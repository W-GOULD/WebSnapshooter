import sys
import nmap
from playwright.sync_api import sync_playwright

def parse_nmap_output(filename):
    nm = nmap.PortScanner()
    nm.analyse_nmap_xml_scan(open(filename, 'r').read())
    http_hosts = []

    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            for protocol in nm[host].all_protocols():
                if protocol == 'tcp':
                    for port in nm[host][protocol].keys():
                        service = nm[host][protocol][port]['name']
                        if service in ['http', 'https']:
                            scheme = service
                            http_hosts.append(f"{scheme}://{host}:{port}")

    return http_hosts

def take_screenshot(url, output_file):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until='networkidle')
        page.screenshot(path=output_file)
        browser.close()

if len(sys.argv) < 2:
    print('Usage: python nmap_screenshot.py <nmap-output-file.xml>')
    sys.exit(1)

nmap_output_file = sys.argv[1]
urls = parse_nmap_output(nmap_output_file)

for url in urls:
    output_file = f"{url.replace('/', '_').replace(':', '_')}.png"
    try:
        take_screenshot(url, output_file)
        print(f"Screenshot saved for {url} as {output_file}")
    except Exception as e:
        print(f"Error taking screenshot for {url}: {e}")

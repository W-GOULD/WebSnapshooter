# WebSnapshooter

WebSnapshooter is a simple, yet effective Python script that takes screenshots of websites discovered from an Nmap output file. It's the perfect tool for web reconnaissance when you're feeling a bit lazy and want to peek at those webpages without actually visiting them.

## Prerequisites

- Python 3.6+
- Nmap (with XML output support)
- Playwright (for browser automation)
- python-nmap (for parsing Nmap output)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/W-GOULD/websnapshooter.git
cd websnapshooter
```

2. Install the required Python libraries:

```bash
pip install python-nmap playwright
```
3. Install Playwright browsers:
```bash
playwright install
```

## Usage
First, run an Nmap scan and save the output in XML format:

```bash
nmap -p80,443 -oX nmap_output.xml <target>
```
Next, run the WebSnapshooter script:

```bash
python nmap_screenshot.py nmap_output.xml
```
The script will parse the Nmap output file, extract the websites with HTTP/HTTPS services, and use Playwright to take screenshots of these websites. The screenshots will be saved in the current directory with the URL as the file name.

Please remember to use this script responsibly and only on systems you have permission to access.

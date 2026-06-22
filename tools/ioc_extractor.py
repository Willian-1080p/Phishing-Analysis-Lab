import re
import sys

if len(sys.argv) < 2:
    print("Usage: python ioc_extractor.py file.txt")
    exit()

with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as file:
    content = file.read()

ips = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', content)
urls = re.findall(r'https?://[^\s]+', content)

print("IPs:")
for ip in set(ips):
    print(ip)

print("\nURLs:")
for url in set(urls):
    print(url)
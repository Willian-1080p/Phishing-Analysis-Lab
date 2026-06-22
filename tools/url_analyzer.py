from urllib.parse import urlparse

url = input("URL: ")

parsed = urlparse(url)

print(f"Scheme: {parsed.scheme}")
print(f"Domain: {parsed.netloc}")
print(f"Path: {parsed.path}")

if "@" in url:
    print("Warning: @ symbol detected")

if len(url) > 100:
    print("Warning: Long URL")
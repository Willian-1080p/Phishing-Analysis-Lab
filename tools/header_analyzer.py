import email
import sys

if len(sys.argv) < 2:
    print("Usage: python header_analyzer.py email.eml")
    exit()

with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
    msg = email.message_from_file(f)

headers = [
    "From",
    "To",
    "Subject",
    "Date",
    "Reply-To",
    "Return-Path"
]

for header in headers:
    print(f"{header}: {msg.get(header)}")
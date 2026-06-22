import json
import sys

if len(sys.argv) < 2:
    print("Usage: python sandbox_report_parser.py report.json")
    exit()

with open(sys.argv[1]) as file:
    report = json.load(file)

print("Summary")
print("=" * 30)

for key in report:
    print(f"{key}: {report[key]}")
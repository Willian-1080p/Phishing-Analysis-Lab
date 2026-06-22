import dns.resolver

domain = input("Domain: ")

records = {
    "SPF": domain,
    "DMARC": f"_dmarc.{domain}",
    "DKIM": f"default._domainkey.{domain}"
}

for name, record in records.items():
    try:
        answers = dns.resolver.resolve(record, "TXT")
        print(f"\n{name}")
        for answer in answers:
            print(answer)
    except:
        print(f"{name} record not found")
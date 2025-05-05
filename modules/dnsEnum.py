from dns.resolver import resolve

def run():
    domain = input("Digite o domínio para enumeração DNS: ").strip()
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]
    for rtype in record_types:
        try:
            answers = resolve(domain, rtype)
            print(f"\n[{rtype}]")
            for answer in answers:
                print(answer)
        except Exception as e:
            print(f"Erro ao obter {rtype}: {e}")

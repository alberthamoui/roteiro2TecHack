import whois

def run():
    domain = input("Digite o domínio (ex: google.com): ").strip()
    try:
        info = whois.whois(domain)
        for key, value in info.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Erro ao consultar WHOIS: {e}")
import requests

def run():
    domain = input("Digite o domínio para buscar subdomínios: ").strip()
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        subdomains = {entry['name_value'] for entry in data}
        print("\nSubdomínios encontrados:")
        for sub in sorted(subdomains):
            print(sub)
    except Exception as e:
        print(f"Erro ao buscar subdomínios: {e}")

import sys
from modules import portscan, whoisLookup, dnsEnum, subDomainEnum, wafDetect

def menu():
    while True:
        print("\n--- Reconhecimento de Alvo ---")
        print("1. PortScan")
        print("2. WHOIS Lookup")
        print("3. DNS Enumeration")
        print("4. Subdomain Enumeration")
        print("5. WAF Detection")
        print("0. Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            portscan.main()
        elif choice == "2":
            whoisLookup.run()
        elif choice == "3":
            dnsEnum.run()
        elif choice == "4":
            subDomainEnum.run()
        elif choice == "5":
            wafDetect.run()
        elif choice == "0":
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

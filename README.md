# roteiro2TecHack - Ferramenta de Reconhecimento para Pentests

Este aplicativo CLI reúne diversas ferramentas utilizadas na fase de reconhecimento de um pentest. Ele foi desenvolvido como parte do projeto da disciplina Tecnologias Hacker.

## 🔧 Funcionalidades

- **PortScan:** Scanner de portas com identificação de banner e sistema operacional.
- **WHOIS Lookup:** Consulta de informações WHOIS de domínios.
- **DNS Enumeration:** Enumeração de registros DNS (A, MX, TXT, NS...).
- **Subdomain Enumeration:** Coleta subdomínios públicos via `crt.sh`.
- **WAF Detection:** Detecção de firewall de aplicações web com `wafw00f`.

## 📦 Instalação

1. Clone o repositório:
    ```bash
   git clone https://github.com/alberthamoui/roteiro2TecHack.git
   cd roteiro2TecHack
    ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script principal:
   ```bash
   python main.py
   ```

## 📚 Uso

* Escolha uma das opções disponíveis no menu principal.
* Siga as instruções na tela para fornecer os parâmetros necessários (como IP, domínio, etc.).
* Aguarde os resultados e analise as informações coletadas.

## ✅ Respostas

1. Além do PortScan, quais são as 5 ferramentas mais úteis para reconhecimento em um pentest? Justifique cada escolha com base em casos reais (ex: Shodan para IoT, theHarvester para e-mails).
    - Shodan
        - Muito bom para encontrar dispositivos IoT expostos na internet.
    - theHarvester
        - Muito bom pra juntar informações publicas sobre um alvo, como emails e subdomínios. Pode ser usada pra levantar possíveis contas para ataques de phishing
    - Amass
        - Muito bom pra enumeração de subdomínios. Funciona passivamente e ativamente, usando APIs e brute force.
    - Nmap
        - Alem de escanear ports, detecta sistemas operacionais e vulnerabilidades.
    - Wappalyzer 
        - Identifica quais tecnologias estão sendo usadas em um site.


2. Qual a diferença entre um scanner de portas SYN e um TCP Connect Scan? Explique em qual cenário cada um é mais eficiente.

3. Como um pentester pode evitar ser detectado por sistemas de prevenção de intrusão (IPS) durante o reconhecimento? Liste técnicas e como elas impactam a eficácia do scan.

## 📁 Evidências

* [✔️ PortScan](evidencias/PortScan.txt)
* [✔️ WHOIS Lookup](evidencias/WHOIS.txt)
* [✔️ DNS Enumeration](evidencias/DNS.txt)
* [✔️ Subdomain Enumeration](evidencias/Subdomain.txt)
* [✔️ WAF Detection](evidencias/WAF.txt)
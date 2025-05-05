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

### 1. Além do PortScan, quais são as 5 ferramentas mais úteis para reconhecimento em um pentest? Justifique cada escolha com base em casos reais (ex: Shodan para IoT, theHarvester para e-mails).
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


### 2. Qual a diferença entre um scanner de portas SYN e um TCP Connect Scan? Explique em qual cenário cada um é mais eficiente.

| Característica              | SYN Scan                                | TCP Connect Scan                                |
| --------------------------- | --------------------------------------- | ----------------------------------------------- |
| Tipo de conexão             | Parcial (não termina o handshake)       | Completa (SYN -> SYN-ACK -> ACK)                  |
| Confiabilidade do resultado | Alta, mas não cria conexão real         | Muito alta (confirma que a conexão foi feita)   |
| Velocidade                  | Mais rápido                             | Mais lento                                      |
| Detecção por firewalls      | Menos detectável (não cria conexão real)| Mais fácil de detectar (não completa a conexão) |
| Permissões                  | Requer privilégios de root/admin        | Não precisa de root/admin                       |
| Ruído na rede               | Baixo                                   | Alto                                            |


- SYN Scan é melhor quando você prioriza velocidade e sigilo, como em redes protegidas por firewalls.
- TCP Connect Scan é melhor quando você não tem acesso root/admin, ou quer garantir 100% que a conexão é possível.


### 3. Como um pentester pode evitar ser detectado por sistemas de prevenção de intrusão (IPS) durante o reconhecimento? Liste técnicas e como elas impactam a eficácia do scan.
```
Scan lento (Timing): 
    - Envia os pacotes com um bom intervalo entre eles, reduz a chance de detecção, mas em consequencia o scan fica bem mais demorado.

Randomização de portas e alvos: 
    - Muda a ordem dos hosts e das portas escaneadas.

Uso de proxies ou VPNs: 
    - Esconde o IP real do atacante durante o scan, ajuda a manter o anonimato.

Fragmentação de pacotes: 
    - Quebra os pacotes em pacotes menores, confunde os sistemas que tentam analisar o conteúdo do tráfego.

SYN Scan: 
    - Envia só o pacote SYN e não completa o handshake TCP, ajuda evitando alertas que seriam gerados por conexões completas.

```


## 📁 Evidências

* [✔️ PortScan](evidencias/PortScan.txt)
* [✔️ WHOIS Lookup](evidencias/WHOIS.txt)
* [✔️ DNS Enumeration](evidencias/DNS.txt)
* [✔️ Subdomain Enumeration](evidencias/Subdomain.txt)
* [✔️ WAF Detection](evidencias/WAF.txt)
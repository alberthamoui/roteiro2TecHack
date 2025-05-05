import subprocess

def run():
    target = input("Digite o alvo (ex: https://exemplo.com): ").strip()
    try:
        result = subprocess.run(["wafw00f", target], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Erro ao executar wafw00f: {e}")

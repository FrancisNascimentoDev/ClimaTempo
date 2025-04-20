"""
Este script cria um ambiente virtual Python e configura o VS Code para usá-lo.
Ele instala automaticamente as dependências do requirements.txt e configura o VS Code.
Deve ser executado no diretório do projeto onde você deseja criar o ambiente virtual.

Para executar o script, use o seguinte comando no terminal:
python setup_venv.py
"""

import os
import sys
import subprocess
import platform

def verificar_requirements():
    """Verifica se o arquivo requirements.txt existe no diretório atual"""
    if not os.path.exists("requirements.txt"):
        print("⚠️ Aviso: Arquivo requirements.txt não encontrado no diretório atual.")
        return False
    return True

def instalar_dependencias():
    """Instala as dependências do requirements.txt no ambiente virtual"""
    print("📦 Instalando dependências do requirements.txt...")
    
    # Comando para instalar dependências, considerando o sistema operacional
    pip_cmd = os.path.abspath("venv/Scripts/pip.exe" if platform.system() == "Windows" else "venv/bin/pip")
    
    try:
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependências instaladas com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False
    return True

def criar_venv():
    """Cria o ambiente virtual Python"""
    print("📦 Criando ambiente virtual...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])

def configurar_vscode():
    """Configura o VS Code para usar o Python da venv"""
    print("🛠️ Configurando VS Code para usar a venv...")
    os.makedirs(".vscode", exist_ok=True)
    
    path = os.path.abspath("venv/Scripts/python.exe" if platform.system() == "Windows" else "venv/bin/python3")
    
    with open(".vscode/settings.json", "w") as f:
        f.write(f'''{{
    "python.pythonPath": "{path}",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "autopep8"
}}''')

def ativar_msg():
    """Mostra mensagem de sucesso e instruções para ativar o ambiente"""
    print("\n✅ Ambiente virtual configurado com sucesso!")
    print("Abra o terminal do VS Code e ative com:")
    
    if platform.system() == "Windows":
        print("venv\\Scripts\\activate")
        print("Ou para PowerShell: .\\venv\\Scripts\\Activate.ps1")
    else:
        print("source venv/bin/activate")
    
    print("\nOu apenas feche e reabra o terminal do VS Code, ele deve reconhecer automaticamente.")

if __name__ == "__main__":
    criar_venv()
    configurar_vscode()
    
    if verificar_requirements():
        instalar_dependencias()
    
    ativar_msg()
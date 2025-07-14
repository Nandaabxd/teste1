#!/usr/bin/env python3
"""
Script para corrigir o SDK Manager no GitHub Actions
Especificamente para resolver o erro: sdkmanager path does not exist
"""

import os
import sys
import subprocess
import urllib.request
import zipfile
import shutil
from pathlib import Path

def print_status(message):
    """Imprime mensagem de status formatada"""
    print(f"🔧 {message}")

def print_error(message):
    """Imprime mensagem de erro formatada"""
    print(f"❌ {message}")

def print_success(message):
    """Imprime mensagem de sucesso formatada"""
    print(f"✅ {message}")

def run_command(cmd, cwd=None):
    """Executa um comando e retorna o resultado"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def fix_sdk_manager_github_actions():
    """Corrige o SDK Manager especificamente para GitHub Actions"""
    print_status("Iniciando correção do SDK Manager para GitHub Actions...")
    
    # Definir caminhos
    home_dir = Path.home()
    buildozer_dir = home_dir / ".buildozer"
    android_dir = buildozer_dir / "android" / "platform"
    sdk_dir = android_dir / "android-sdk"
    
    # Criar diretórios necessários
    android_dir.mkdir(parents=True, exist_ok=True)
    sdk_dir.mkdir(parents=True, exist_ok=True)
    
    print_status(f"Diretórios criados: {android_dir}")
    
    # URL do SDK Command Line Tools mais recente
    cmdline_tools_url = "https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip"
    cmdline_tools_zip = android_dir / "commandlinetools.zip"
    
    # Baixar command line tools
    print_status("Baixando SDK Command Line Tools...")
    try:
        urllib.request.urlretrieve(cmdline_tools_url, cmdline_tools_zip)
        print_success(f"Download concluído: {cmdline_tools_zip}")
    except Exception as e:
        print_error(f"Erro ao baixar SDK Command Line Tools: {e}")
        return False
    
    # Extrair command line tools
    print_status("Extraindo SDK Command Line Tools...")
    try:
        with zipfile.ZipFile(cmdline_tools_zip, 'r') as zip_ref:
            zip_ref.extractall(android_dir)
        print_success("Extração concluída")
    except Exception as e:
        print_error(f"Erro ao extrair: {e}")
        return False
    
    # Reorganizar estrutura de diretórios
    print_status("Reorganizando estrutura de diretórios...")
    extracted_cmdline_tools = android_dir / "cmdline-tools"
    sdk_cmdline_tools = sdk_dir / "cmdline-tools"
    latest_dir = sdk_cmdline_tools / "latest"
    
    # Criar estrutura correta
    sdk_cmdline_tools.mkdir(parents=True, exist_ok=True)
    
    # Mover cmdline-tools para a estrutura correta
    if extracted_cmdline_tools.exists():
        if latest_dir.exists():
            shutil.rmtree(latest_dir)
        shutil.move(str(extracted_cmdline_tools), str(latest_dir))
        print_success("Estrutura reorganizada")
    
    # Limpar arquivo ZIP
    if cmdline_tools_zip.exists():
        cmdline_tools_zip.unlink()
    
    # Definir variáveis de ambiente
    os.environ['ANDROID_SDK_ROOT'] = str(sdk_dir)
    os.environ['ANDROID_HOME'] = str(sdk_dir)
    os.environ['PATH'] = f"{latest_dir}/bin:{os.environ.get('PATH', '')}"
    
    print_status("Variáveis de ambiente configuradas")
    
    # Verificar se o sdkmanager está funcionando
    sdkmanager_path = latest_dir / "bin" / "sdkmanager"
    if sdkmanager_path.exists():
        print_success(f"SDK Manager encontrado: {sdkmanager_path}")
        
        # Tornar executável
        os.chmod(sdkmanager_path, 0o755)
        
        # Testar sdkmanager
        print_status("Testando SDK Manager...")
        success, stdout, stderr = run_command(f"{sdkmanager_path} --version")
        if success:
            print_success(f"SDK Manager funcionando: {stdout.strip()}")
            
            # Aceitar licenças
            print_status("Aceitando licenças do Android SDK...")
            license_cmd = f"yes | {sdkmanager_path} --licenses"
            success, stdout, stderr = run_command(license_cmd)
            if success:
                print_success("Licenças aceitas")
            else:
                print_error(f"Erro ao aceitar licenças: {stderr}")
            
            # Instalar componentes necessários
            print_status("Instalando componentes do SDK...")
            components = [
                "platform-tools",
                "platforms;android-33",
                "build-tools;33.0.2"
            ]
            
            for component in components:
                print_status(f"Instalando {component}...")
                install_cmd = f"{sdkmanager_path} '{component}'"
                success, stdout, stderr = run_command(install_cmd)
                if success:
                    print_success(f"{component} instalado")
                else:
                    print_error(f"Erro ao instalar {component}: {stderr}")
            
            return True
        else:
            print_error(f"SDK Manager não está funcionando: {stderr}")
            return False
    else:
        print_error("SDK Manager não encontrado após instalação")
        return False

def main():
    """Função principal"""
    print_status("🚀 Iniciando correção do SDK Manager...")
    
    if fix_sdk_manager_github_actions():
        print_success("✅ SDK Manager corrigido com sucesso!")
        
        # Mostrar estrutura final
        print_status("Estrutura final do SDK:")
        sdk_dir = Path.home() / ".buildozer" / "android" / "platform" / "android-sdk"
        for item in sdk_dir.rglob("*"):
            if item.is_file() and "sdkmanager" in item.name:
                print(f"  📄 {item}")
        
        return 0
    else:
        print_error("❌ Falha na correção do SDK Manager")
        return 1

if __name__ == "__main__":
    sys.exit(main())

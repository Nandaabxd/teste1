#!/usr/bin/env python3
"""
Script para corrigir problemas com o SDK Manager durante o build do APK.
Este script vai baixar e configurar o SDK Manager corretamente.
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
    print(f"[INFO] {message}")

def print_error(message):
    """Imprime mensagem de erro formatada"""
    print(f"[ERRO] {message}")

def download_file(url, dest_path):
    """Baixa um arquivo da URL para o destino"""
    print_status(f"Baixando {url}...")
    try:
        urllib.request.urlretrieve(url, dest_path)
        print_status(f"Download concluído: {dest_path}")
        return True
    except Exception as e:
        print_error(f"Erro ao baixar {url}: {e}")
        return False

def extract_zip(zip_path, extract_to):
    """Extrai um arquivo ZIP"""
    print_status(f"Extraindo {zip_path}...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print_status(f"Extração concluída em: {extract_to}")
        return True
    except Exception as e:
        print_error(f"Erro ao extrair {zip_path}: {e}")
        return False

def fix_sdk_manager():
    """Corrige o problema do SDK Manager"""
    print_status("Iniciando correção do SDK Manager...")
    
    # Caminhos importantes
    buildozer_dir = Path.home() / ".buildozer"
    android_dir = buildozer_dir / "android" / "platform"
    sdk_dir = android_dir / "android-sdk"
    
    # Criar diretórios se não existirem
    android_dir.mkdir(parents=True, exist_ok=True)
    
    # URL do SDK Command Line Tools
    cmdline_tools_url = "https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip"
    cmdline_tools_zip = android_dir / "commandlinetools.zip"
    
    # Baixar command line tools
    if not download_file(cmdline_tools_url, cmdline_tools_zip):
        return False
    
    # Extrair command line tools
    cmdline_tools_dir = android_dir / "cmdline-tools"
    if not extract_zip(cmdline_tools_zip, cmdline_tools_dir):
        return False
    
    # Reorganizar estrutura de diretórios
    extracted_dir = cmdline_tools_dir / "cmdline-tools"
    latest_dir = cmdline_tools_dir / "latest"
    
    if extracted_dir.exists():
        if latest_dir.exists():
            shutil.rmtree(latest_dir)
        extracted_dir.rename(latest_dir)
    
    # Criar diretório do SDK se não existir
    sdk_dir.mkdir(parents=True, exist_ok=True)
    
    # Mover cmdline-tools para dentro do SDK
    sdk_cmdline_tools = sdk_dir / "cmdline-tools"
    if sdk_cmdline_tools.exists():
        shutil.rmtree(sdk_cmdline_tools)
    
    shutil.move(str(cmdline_tools_dir), str(sdk_cmdline_tools))
    
    # Limpar arquivo ZIP
    if cmdline_tools_zip.exists():
        cmdline_tools_zip.unlink()
    
    print_status("SDK Manager corrigido com sucesso!")
    
    # Verificar se o sdkmanager está funcionando
    sdkmanager_path = sdk_dir / "cmdline-tools" / "latest" / "bin" / "sdkmanager"
    if sdkmanager_path.exists():
        print_status(f"SDK Manager encontrado em: {sdkmanager_path}")
        return True
    else:
        print_error("SDK Manager não encontrado após a correção")
        return False

def update_buildozer_spec():
    """Atualiza o buildozer.spec com as configurações corretas"""
    print_status("Atualizando buildozer.spec...")
    
    spec_file = Path("buildozer.spec")
    if not spec_file.exists():
        print_error("Arquivo buildozer.spec não encontrado")
        return False
    
    # Ler o arquivo atual
    with open(spec_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Configurações para adicionar/atualizar
    updates = {
        'android.cmdline_tools': '9.0',
        'android.auto_accept_licenses': 'True',
        'android.sdk': '33',
        'android.build_tools': '33.0.2',
        'android.api': '33',
        'android.minapi': '21',
        'android.ndk': '25b'
    }
    
    # Aplicar atualizações
    for key, value in updates.items():
        pattern = f"{key} = "
        if pattern in content:
            # Atualizar valor existente
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith(pattern):
                    lines[i] = f"{key} = {value}"
                    break
            content = '\n'.join(lines)
        else:
            # Adicionar nova configuração
            content += f"\n{key} = {value}\n"
    
    # Salvar arquivo atualizado
    with open(spec_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print_status("buildozer.spec atualizado com sucesso!")
    return True

def main():
    """Função principal"""
    print_status("=== Correção do SDK Manager para Buildozer ===")
    
    # Verificar se estamos no Linux (necessário para o build)
    if sys.platform == "win32":
        print_error("Este script deve ser executado no Linux (WSL, GitHub Actions, etc.)")
        print_status("Use o WSL ou GitHub Actions para compilar o APK")
        return
    
    # Corrigir SDK Manager
    if not fix_sdk_manager():
        print_error("Falha ao corrigir o SDK Manager")
        sys.exit(1)
    
    # Atualizar buildozer.spec
    if not update_buildozer_spec():
        print_error("Falha ao atualizar buildozer.spec")
        sys.exit(1)
    
    print_status("Correção concluída com sucesso!")
    print_status("Agora você pode executar: buildozer android debug")

if __name__ == "__main__":
    main()

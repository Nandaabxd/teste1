# Script PowerShell para preparar ambiente Windows para build Android
# Este script configura o WSL e prepara o ambiente para compilação do APK

param(
    [switch]$InstallWSL,
    [switch]$SetupEnvironment,
    [switch]$RunBuild
)

# Função para log colorido
function Write-ColorOutput($ForegroundColor, $Message) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    Write-Output $Message
    $host.UI.RawUI.ForegroundColor = $fc
}

function Write-Info($Message) {
    Write-ColorOutput "Cyan" "[INFO] $Message"
}

function Write-Success($Message) {
    Write-ColorOutput "Green" "[SUCCESS] $Message"
}

function Write-Warning($Message) {
    Write-ColorOutput "Yellow" "[WARNING] $Message"
}

function Write-Error($Message) {
    Write-ColorOutput "Red" "[ERROR] $Message"
}

# Função para verificar se o WSL está instalado
function Test-WSL {
    try {
        $wslStatus = wsl --status 2>$null
        return $true
    } catch {
        return $false
    }
}

# Função para instalar WSL
function Install-WSL {
    Write-Info "Instalando WSL..."
    
    # Verificar se já está instalado
    if (Test-WSL) {
        Write-Success "WSL já está instalado!"
        return
    }
    
    try {
        # Instalar WSL
        Write-Info "Instalando WSL 2..."
        wsl --install -d Ubuntu
        
        Write-Success "WSL instalado com sucesso!"
        Write-Warning "Você precisa reiniciar o computador para completar a instalação."
        Write-Info "Após reiniciar, execute novamente com -SetupEnvironment"
        
    } catch {
        Write-Error "Erro ao instalar WSL: $_"
        Write-Info "Tente instalar manualmente pelo Microsoft Store"
    }
}

# Função para configurar o ambiente no WSL
function Setup-WSLEnvironment {
    Write-Info "Configurando ambiente WSL para build Android..."
    
    # Verificar se WSL está disponível
    if (-not (Test-WSL)) {
        Write-Error "WSL não está instalado. Execute com -InstallWSL primeiro."
        return
    }
    
    # Verificar se Ubuntu está instalado
    $ubuntuInstalled = wsl -l -v | Select-String "Ubuntu"
    if (-not $ubuntuInstalled) {
        Write-Error "Ubuntu não está instalado no WSL."
        Write-Info "Instale Ubuntu pelo Microsoft Store ou execute: wsl --install -d Ubuntu"
        return
    }
    
    # Script para executar no WSL
    $wslScript = @"
#!/bin/bash
set -e

echo "[INFO] Atualizando sistema..."
sudo apt-get update -y
sudo apt-get upgrade -y

echo "[INFO] Instalando dependências do sistema..."
sudo apt-get install -y git zip unzip openjdk-11-jdk python3-pip python3-venv
sudo apt-get install -y libffi-dev libssl-dev build-essential
sudo apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev
sudo apt-get install -y libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev
sudo apt-get install -y zlib1g-dev liblzma-dev wget curl

echo "[INFO] Instalando Python dependencies..."
pip3 install --user buildozer cython

echo "[INFO] Configurando JAVA_HOME..."
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
echo 'export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc

echo "[INFO] Ambiente WSL configurado com sucesso!"
echo "[INFO] Execute 'source ~/.bashrc' para recarregar o ambiente"
"@
    
    # Salvar script temporário
    $tempScript = "$env:TEMP\setup_wsl.sh"
    $wslScript | Out-File -FilePath $tempScript -Encoding utf8
    
    # Copiar script para WSL e executar
    try {
        Write-Info "Copiando arquivos para WSL..."
        
        # Copiar projeto para WSL
        $projectPath = (Get-Location).Path
        $wslProjectPath = "/home/$(wsl whoami)/nfc-writer-pro"
        
        wsl mkdir -p $wslProjectPath
        wsl cp -r /mnt/c/Users/maria/OneDrive/Desktop/teste1/* $wslProjectPath/
        
        # Copiar e executar script de configuração
        wsl cp /mnt/c/Users/maria/AppData/Local/Temp/setup_wsl.sh /tmp/
        wsl chmod +x /tmp/setup_wsl.sh
        wsl /tmp/setup_wsl.sh
        
        # Limpar script temporário
        Remove-Item $tempScript -Force
        
        Write-Success "Ambiente WSL configurado com sucesso!"
        Write-Info "Projeto copiado para: $wslProjectPath"
        
    } catch {
        Write-Error "Erro ao configurar ambiente WSL: $_"
        if (Test-Path $tempScript) {
            Remove-Item $tempScript -Force
        }
    }
}

# Função para executar build no WSL
function Start-WSLBuild {
    Write-Info "Iniciando build no WSL..."
    
    # Verificar se WSL está disponível
    if (-not (Test-WSL)) {
        Write-Error "WSL não está instalado. Execute com -InstallWSL primeiro."
        return
    }
    
    $wslBuildScript = @"
#!/bin/bash
set -e

# Navegar para o projeto
cd /home/$(whoami)/nfc-writer-pro

# Configurar ambiente
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
source ~/.bashrc

echo "[INFO] Executando correção do SDK Manager..."
python3 fix_sdk_manager.py

echo "[INFO] Iniciando build do APK..."
chmod +x monitor_build_fixed.sh
./monitor_build_fixed.sh

echo "[INFO] Build concluído!"
if [ -f "bin/nfcwriterpro2-2.0-armeabi-v7a-debug.apk" ]; then
    echo "[SUCCESS] APK criado: bin/nfcwriterpro2-2.0-armeabi-v7a-debug.apk"
    ls -lh bin/*.apk
else
    echo "[ERROR] APK não foi criado!"
    exit 1
fi
"@
    
    # Salvar script temporário
    $tempBuildScript = "$env:TEMP\build_wsl.sh"
    $wslBuildScript | Out-File -FilePath $tempBuildScript -Encoding utf8
    
    try {
        # Copiar e executar script de build
        wsl cp /mnt/c/Users/maria/AppData/Local/Temp/build_wsl.sh /tmp/
        wsl chmod +x /tmp/build_wsl.sh
        wsl /tmp/build_wsl.sh
        
        # Copiar APK de volta para Windows
        Write-Info "Copiando APK para Windows..."
        $wslProjectPath = "/home/$(wsl whoami)/nfc-writer-pro"
        wsl cp $wslProjectPath/bin/*.apk /mnt/c/Users/maria/OneDrive/Desktop/teste1/
        
        # Limpar script temporário
        Remove-Item $tempBuildScript -Force
        
        Write-Success "Build concluído com sucesso!"
        Write-Info "APK copiado para: $(Get-Location)"
        
        # Mostrar arquivos APK criados
        $apkFiles = Get-ChildItem -Path "." -Filter "*.apk"
        if ($apkFiles) {
            Write-Success "Arquivos APK criados:"
            foreach ($apk in $apkFiles) {
                Write-Info "  - $($apk.Name) ($(($apk.Length / 1MB).ToString('F2')) MB)"
            }
        }
        
    } catch {
        Write-Error "Erro durante o build: $_"
        if (Test-Path $tempBuildScript) {
            Remove-Item $tempBuildScript -Force
        }
    }
}

# Função para mostrar ajuda
function Show-Help {
    Write-Info "=== Script de Build Android para Windows ==="
    Write-Info ""
    Write-Info "Uso: .\build_windows.ps1 [opções]"
    Write-Info ""
    Write-Info "Opções:"
    Write-Info "  -InstallWSL        Instala WSL (requer reinicialização)"
    Write-Info "  -SetupEnvironment  Configura ambiente WSL para build"
    Write-Info "  -RunBuild          Executa build do APK no WSL"
    Write-Info ""
    Write-Info "Exemplos:"
    Write-Info "  .\build_windows.ps1 -InstallWSL"
    Write-Info "  .\build_windows.ps1 -SetupEnvironment"
    Write-Info "  .\build_windows.ps1 -RunBuild"
    Write-Info ""
    Write-Info "Processo completo:"
    Write-Info "  1. Execute com -InstallWSL (reinicie após instalação)"
    Write-Info "  2. Execute com -SetupEnvironment"
    Write-Info "  3. Execute com -RunBuild"
}

# Função principal
function Main {
    Write-Info "=== Build Android APK para Windows ==="
    
    # Verificar se está executando como administrador para WSL
    if ($InstallWSL) {
        $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
        $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
        if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
            Write-Error "Para instalar WSL, execute como Administrador!"
            return
        }
    }
    
    # Executar ação solicitada
    if ($InstallWSL) {
        Install-WSL
    } elseif ($SetupEnvironment) {
        Setup-WSLEnvironment
    } elseif ($RunBuild) {
        Start-WSLBuild
    } else {
        Show-Help
    }
}

# Executar função principal
Main

# Script PowerShell para configurar ambiente de compilação APK
# Execute como Administrador

Write-Host "=== Configuração do Ambiente para Compilar APK Android ===" -ForegroundColor Green
Write-Host "Este script irá configurar o WSL para compilar o APK" -ForegroundColor Yellow

# Verifica se está executando como administrador
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "ERRO: Este script deve ser executado como Administrador!" -ForegroundColor Red
    Write-Host "Clique com o botão direito no PowerShell e selecione 'Executar como Administrador'" -ForegroundColor Red
    pause
    exit 1
}

# 1. Instalar WSL se não estiver instalado
Write-Host "1. Verificando WSL..." -ForegroundColor Blue
$wslStatus = wsl --status 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Instalando WSL..." -ForegroundColor Yellow
    wsl --install
    Write-Host "WSL instalado! Reinicie o computador e execute este script novamente." -ForegroundColor Green
    pause
    exit 0
}

# 2. Verificar se Ubuntu está instalado
Write-Host "2. Verificando Ubuntu..." -ForegroundColor Blue
$ubuntuCheck = wsl -l -v | Select-String "Ubuntu"
if (-not $ubuntuCheck) {
    Write-Host "Instalando Ubuntu..." -ForegroundColor Yellow
    wsl --install -d Ubuntu
}

# 3. Configurar ambiente no Ubuntu
Write-Host "3. Configurando ambiente no Ubuntu..." -ForegroundColor Blue
$setupScript = @"
#!/bin/bash
echo "=== Configurando ambiente para compilar APK ==="

# Atualizar sistema
echo "Atualizando sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar dependências
echo "Instalando dependências..."
sudo apt install -y python3-pip python3-venv git openjdk-8-jdk unzip build-essential libssl-dev libffi-dev python3-dev

# Instalar Buildozer
echo "Instalando Buildozer..."
pip3 install buildozer

# Criar diretório para o projeto
echo "Criando diretório do projeto..."
mkdir -p ~/nfc-app

echo "=== Configuração concluída! ==="
echo "Agora você pode copiar os arquivos do projeto para ~/nfc-app e executar:"
echo "cd ~/nfc-app && buildozer android debug"
"@

# Salvar script no WSL
$setupScript | wsl bash

Write-Host "4. Copiando arquivos do projeto..." -ForegroundColor Blue
$projectPath = "C:\Users\maria\OneDrive\Desktop\teste1"
wsl -- cp -r "/mnt/c/Users/maria/OneDrive/Desktop/teste1" "~/nfc-app"

Write-Host "=== Configuração Concluída! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Próximos passos:" -ForegroundColor Yellow
Write-Host "1. Abra o Ubuntu (WSL) no menu iniciar"
Write-Host "2. Execute: cd ~/nfc-app"
Write-Host "3. Execute: buildozer android debug"
Write-Host "4. Aguarde a compilação (pode demorar 30-60 minutos na primeira vez)"
Write-Host "5. O APK estará em ~/nfc-app/bin/nfcreader-0.1-debug.apk"
Write-Host ""
Write-Host "Para copiar o APK de volta para o Windows:" -ForegroundColor Cyan
Write-Host "cp ~/nfc-app/bin/*.apk /mnt/c/Users/maria/OneDrive/Desktop/teste1/"
Write-Host ""
pause

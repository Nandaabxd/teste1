#!/bin/bash

# Script de monitoramento para build do APK com correção do SDK Manager
# Este script monitora o progresso do build e aplica correções se necessário

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para log formatado
log() {
    echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Função para verificar se o SDK Manager está disponível
check_sdk_manager() {
    local sdk_path="$HOME/.buildozer/android/platform/android-sdk"
    local sdkmanager_path="$sdk_path/cmdline-tools/latest/bin/sdkmanager"
    
    if [ -f "$sdkmanager_path" ]; then
        log_success "SDK Manager encontrado em: $sdkmanager_path"
        return 0
    else
        log_error "SDK Manager não encontrado em: $sdkmanager_path"
        return 1
    fi
}

# Função para corrigir o SDK Manager
fix_sdk_manager() {
    log "Iniciando correção do SDK Manager..."
    
    local android_dir="$HOME/.buildozer/android/platform"
    local sdk_dir="$android_dir/android-sdk"
    
    # Criar diretórios
    mkdir -p "$android_dir"
    cd "$android_dir"
    
    # Baixar SDK Command Line Tools
    log "Baixando SDK Command Line Tools..."
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip
    
    # Extrair e organizar
    log "Extraindo e organizando SDK Command Line Tools..."
    unzip -q commandlinetools-linux-9477386_latest.zip
    
    # Criar estrutura correta
    mkdir -p "$sdk_dir/cmdline-tools"
    mv cmdline-tools "$sdk_dir/cmdline-tools/latest"
    
    # Configurar permissões
    chmod +x "$sdk_dir/cmdline-tools/latest/bin/sdkmanager"
    
    # Limpar arquivo ZIP
    rm commandlinetools-linux-9477386_latest.zip
    
    log_success "SDK Manager corrigido com sucesso!"
}

# Função para configurar o ambiente Android
setup_android_env() {
    log "Configurando ambiente Android..."
    
    export ANDROID_SDK_ROOT="$HOME/.buildozer/android/platform/android-sdk"
    export PATH="$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$PATH"
    export PATH="$ANDROID_SDK_ROOT/platform-tools:$PATH"
    
    # Aceitar licenças
    log "Aceitando licenças do Android SDK..."
    yes | sdkmanager --licenses >/dev/null 2>&1
    
    # Instalar componentes necessários
    log "Instalando componentes do Android SDK..."
    sdkmanager "platform-tools" >/dev/null 2>&1
    sdkmanager "platforms;android-33" >/dev/null 2>&1
    sdkmanager "build-tools;33.0.2" >/dev/null 2>&1
    
    log_success "Ambiente Android configurado!"
}

# Função para monitorar o build
monitor_build() {
    log "Iniciando monitoramento do build..."
    
    local log_file="/tmp/buildozer_build.log"
    
    # Executar buildozer em background e capturar output
    buildozer android debug --verbose 2>&1 | tee "$log_file" &
    local build_pid=$!
    
    # Monitorar progresso
    while kill -0 $build_pid 2>/dev/null; do
        sleep 5
        
        # Verificar se há erros conhecidos
        if tail -20 "$log_file" | grep -q "sdkmanager.*does not exist"; then
            log_error "Erro do SDK Manager detectado!"
            kill $build_pid 2>/dev/null || true
            return 1
        fi
        
        # Mostrar progresso
        local last_line=$(tail -1 "$log_file" | tr -d '\n')
        if [[ ! -z "$last_line" ]]; then
            echo -ne "\r${BLUE}[BUILD]${NC} $last_line"
        fi
    done
    
    echo # Nova linha após o progresso
    
    # Verificar resultado
    wait $build_pid
    local exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        log_success "Build concluído com sucesso!"
        return 0
    else
        log_error "Build falhou com código de saída: $exit_code"
        return 1
    fi
}

# Função principal
main() {
    log "=== Monitoramento de Build APK com Correção do SDK Manager ==="
    
    # Verificar se estamos no Linux
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        log_error "Este script deve ser executado no Linux (WSL, GitHub Actions, etc.)"
        log_warning "Use o WSL ou GitHub Actions para compilar o APK"
        exit 1
    fi
    
    # Verificar se buildozer está instalado
    if ! command -v buildozer &> /dev/null; then
        log_error "Buildozer não está instalado"
        log "Instalando buildozer..."
        pip install buildozer cython
    fi
    
    # Verificar SDK Manager
    if ! check_sdk_manager; then
        log "Corrigindo SDK Manager..."
        fix_sdk_manager
        
        if ! check_sdk_manager; then
            log_error "Falha ao corrigir SDK Manager"
            exit 1
        fi
    fi
    
    # Configurar ambiente
    setup_android_env
    
    # Monitorar build
    if monitor_build; then
        log_success "Build concluído! Verifique o arquivo APK em bin/"
        
        # Mostrar informações do APK
        if [ -f "bin/nfcwriterpro2-2.0-armeabi-v7a-debug.apk" ]; then
            local apk_size=$(du -h "bin/nfcwriterpro2-2.0-armeabi-v7a-debug.apk" | cut -f1)
            log_success "APK criado: bin/nfcwriterpro2-2.0-armeabi-v7a-debug.apk (${apk_size})"
        fi
    else
        log_error "Build falhou!"
        
        # Mostrar logs de erro
        echo -e "\n${RED}=== ÚLTIMAS LINHAS DO LOG ===${NC}"
        tail -50 /tmp/buildozer_build.log
        
        exit 1
    fi
}

# Executar se chamado diretamente
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

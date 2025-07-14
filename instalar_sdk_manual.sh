#!/bin/bash
# Script para instalar Android SDK manualmente
# Execute no WSL/Linux

echo "🚀 Instalando Android SDK para NFC Writer PRO2..."

# Criar diretórios
mkdir -p ~/.buildozer/android/platform
cd ~/.buildozer/android/platform

# 1. Baixar Command Line Tools
echo "📥 Baixando SDK Command Line Tools..."
wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip

# 2. Extrair e organizar
echo "📦 Extraindo Command Line Tools..."
unzip commandlinetools-linux-11076708_latest.zip
mkdir -p android-sdk/cmdline-tools
mv cmdline-tools android-sdk/cmdline-tools/latest

# 3. Configurar variáveis de ambiente
export ANDROID_SDK_ROOT="$HOME/.buildozer/android/platform/android-sdk"
export ANDROID_HOME="$ANDROID_SDK_ROOT"
export PATH="$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$PATH"

# 4. Aceitar licenças
echo "🔑 Aceitando licenças..."
yes | sdkmanager --licenses

# 5. Instalar componentes necessários
echo "📱 Instalando componentes do SDK..."
sdkmanager "platform-tools"
sdkmanager "platforms;android-33"
sdkmanager "build-tools;33.0.2"

# 6. Baixar NDK
echo "🔧 Baixando Android NDK..."
wget https://dl.google.com/android/repository/android-ndk-r25b-linux.zip
unzip android-ndk-r25b-linux.zip
mv android-ndk-r25b ./

# 7. Limpeza
rm -f *.zip

echo "✅ Android SDK instalado com sucesso!"
echo "📋 Componentes instalados:"
echo "  - Command Line Tools 11.0"
echo "  - Platform API 33 (Android 13)"
echo "  - Build Tools 33.0.2"
echo "  - Platform Tools"
echo "  - NDK 25b"

# Verificar instalação
echo "🔍 Verificando instalação..."
ls -la $ANDROID_SDK_ROOT/
ls -la $ANDROID_SDK_ROOT/build-tools/
ls -la $ANDROID_SDK_ROOT/platforms/

echo "🎉 Pronto para compilar o APK!"

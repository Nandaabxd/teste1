#!/bin/bash

# Script para construir o APK usando Buildozer

echo "=== Configuração do Ambiente para Build Android ==="
echo "Instalando dependências..."

# Instalar buildozer se não estiver instalado
pip install buildozer

echo "=== Iniciando Build do APK ==="
echo "Isso pode demorar alguns minutos na primeira vez..."

# Inicializar buildozer (cria os diretórios necessários)
buildozer init

# Compilar o APK em modo debug
buildozer android debug

echo "=== Build Concluído ==="
echo "O APK deve estar em: ./bin/nfcreader-0.1-debug.apk"

#!/bin/bash

echo "=== Monitor de Compilação APK ==="
echo "Data: $(date)"
echo "================================="

# Verificar se buildozer está rodando
if pgrep -f buildozer > /dev/null; then
    echo "✅ Buildozer está rodando"
    
    # Mostrar última linha do log
    if [ -f .buildozer/logs/buildozer.log ]; then
        echo "📋 Último log:"
        tail -3 .buildozer/logs/buildozer.log
    fi
    
    # Mostrar uso de CPU/RAM
    echo "💻 Uso de recursos:"
    ps aux | grep buildozer | head -1
    
    # Verificar tamanho dos diretórios
    echo "📁 Tamanho .buildozer:"
    du -sh .buildozer/ 2>/dev/null || echo "Diretório ainda não criado"
    
    echo "📦 Procurando APK:"
    find bin/ -name "*.apk" 2>/dev/null || echo "APK ainda não gerado"
    
else
    echo "❌ Buildozer não está rodando"
    
    # Verificar se APK foi gerado
    if [ -d "bin" ]; then
        echo "📦 Verificando APK gerado:"
        ls -la bin/
    fi
fi

echo "================================="
echo "Para monitorar em tempo real:"
echo "tail -f .buildozer/logs/buildozer.log"

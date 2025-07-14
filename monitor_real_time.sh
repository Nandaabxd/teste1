#!/bin/bash

# Monitor de compilação APK
while true; do
    clear
    echo "=== MONITOR DE COMPILAÇÃO APK ==="
    echo "Data: $(date)"
    echo "==============================="
    
    # Verificar se buildozer está rodando
    if pgrep -f buildozer > /dev/null; then
        echo "✅ Status: COMPILANDO"
        
        # Mostrar processo
        echo "💻 Processo:"
        ps aux | grep buildozer | grep -v grep | head -1
        
        # Mostrar tamanho
        echo "📁 Tamanho .buildozer:"
        du -sh .buildozer/ 2>/dev/null || echo "N/A"
        
        # Verificar APK
        echo "📦 APK:"
        if find bin/ -name "*.apk" 2>/dev/null; then
            echo "✅ APK GERADO!"
            ls -la bin/*.apk
        else
            echo "⏳ APK ainda não gerado"
        fi
        
        # Mostrar última atividade
        echo "📋 Última atividade:"
        ls -lat .buildozer/ 2>/dev/null | head -3
        
    else
        echo "❌ Status: PARADO"
        
        # Verificar se APK foi gerado
        if find bin/ -name "*.apk" 2>/dev/null; then
            echo "✅ COMPILAÇÃO CONCLUÍDA!"
            echo "📦 APK encontrado:"
            ls -la bin/*.apk
        else
            echo "❌ Buildozer não está rodando e APK não foi gerado"
        fi
    fi
    
    echo "==============================="
    echo "Pressione Ctrl+C para sair"
    echo "Atualizando em 5 segundos..."
    sleep 5
done

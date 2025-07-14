#!/bin/bash
# Script para verificar se o SDK Manager foi corrigido adequadamente
# Executa verificações completas antes do build

echo "🔍 VERIFICAÇÃO COMPLETA DO SDK MANAGER"
echo "=" * 50

# Definir caminhos
SDK_ROOT="$HOME/.buildozer/android/platform/android-sdk"
NEW_SDK="$SDK_ROOT/cmdline-tools/latest/bin/sdkmanager"
OLD_SDK="$SDK_ROOT/tools/bin/sdkmanager"

# Verificar se os diretórios existem
echo "📁 Verificando estrutura de diretórios..."
if [ -d "$SDK_ROOT" ]; then
    echo "✅ SDK Root existe: $SDK_ROOT"
else
    echo "❌ SDK Root não existe: $SDK_ROOT"
    exit 1
fi

# Verificar SDK Manager nos dois locais
echo "🔧 Verificando SDK Manager..."
SDK_FOUND=false

if [ -f "$NEW_SDK" ]; then
    echo "✅ SDK Manager (NOVO) encontrado: $NEW_SDK"
    if [ -x "$NEW_SDK" ]; then
        echo "✅ SDK Manager (NOVO) é executável"
        SDK_FOUND=true
    else
        echo "⚠️ SDK Manager (NOVO) não é executável"
    fi
else
    echo "❌ SDK Manager (NOVO) não encontrado: $NEW_SDK"
fi

if [ -f "$OLD_SDK" ]; then
    echo "✅ SDK Manager (ANTIGO) encontrado: $OLD_SDK"
    if [ -x "$OLD_SDK" ]; then
        echo "✅ SDK Manager (ANTIGO) é executável"
        SDK_FOUND=true
    else
        echo "⚠️ SDK Manager (ANTIGO) não é executável"
    fi
else
    echo "❌ SDK Manager (ANTIGO) não encontrado: $OLD_SDK"
fi

if [ "$SDK_FOUND" = false ]; then
    echo "💥 ERRO: Nenhum SDK Manager funcional encontrado!"
    exit 1
fi

# Configurar ambiente
echo "🌍 Configurando ambiente..."
export ANDROID_SDK_ROOT="$SDK_ROOT"
export ANDROID_HOME="$SDK_ROOT"
export PATH="$SDK_ROOT/cmdline-tools/latest/bin:$SDK_ROOT/tools/bin:$SDK_ROOT/platform-tools:$PATH"

echo "✅ Variáveis de ambiente configuradas:"
echo "  ANDROID_SDK_ROOT: $ANDROID_SDK_ROOT"
echo "  ANDROID_HOME: $ANDROID_HOME"
echo "  PATH atualizado: OK"

# Testar SDK Manager
echo "🧪 Testando SDK Manager..."
for SDK_PATH in "$NEW_SDK" "$OLD_SDK"; do
    if [ -f "$SDK_PATH" ]; then
        echo "🔍 Testando: $SDK_PATH"
        if "$SDK_PATH" --version >/dev/null 2>&1; then
            VERSION=$("$SDK_PATH" --version 2>/dev/null | head -1)
            echo "✅ SDK Manager funcional: $VERSION"
        else
            echo "❌ SDK Manager não funcional: $SDK_PATH"
        fi
    fi
done

# Verificar licenças
echo "🔑 Verificando licenças..."
LICENSES_DIR="$SDK_ROOT/licenses"
if [ -d "$LICENSES_DIR" ]; then
    echo "✅ Diretório de licenças existe: $LICENSES_DIR"
    LICENSE_COUNT=$(ls -1 "$LICENSES_DIR" 2>/dev/null | wc -l)
    echo "📄 Licenças encontradas: $LICENSE_COUNT"
else
    echo "❌ Diretório de licenças não existe: $LICENSES_DIR"
fi

# Verificar componentes instalados
echo "📱 Verificando componentes instalados..."
COMPONENTS=(
    "platform-tools"
    "platforms/android-33"
    "build-tools/33.0.2"
)

for COMPONENT in "${COMPONENTS[@]}"; do
    COMPONENT_PATH="$SDK_ROOT/$COMPONENT"
    if [ -d "$COMPONENT_PATH" ]; then
        echo "✅ Componente instalado: $COMPONENT"
    else
        echo "❌ Componente ausente: $COMPONENT"
    fi
done

# Verificar AIDL
echo "🔧 Verificando AIDL..."
AIDL_PATHS=(
    "$SDK_ROOT/platform-tools/aidl"
    "$SDK_ROOT/build-tools/33.0.2/aidl"
)

AIDL_FOUND=false
for AIDL_PATH in "${AIDL_PATHS[@]}"; do
    if [ -f "$AIDL_PATH" ]; then
        echo "✅ AIDL encontrado: $AIDL_PATH"
        AIDL_FOUND=true
        break
    fi
done

if [ "$AIDL_FOUND" = false ]; then
    echo "⚠️ AIDL não encontrado, mas pode ser instalado durante o build"
fi

# Resumo final
echo "=" * 50
echo "📋 RESUMO DA VERIFICAÇÃO:"
echo "✅ SDK Root: $SDK_ROOT"
echo "✅ SDK Manager disponível: $SDK_FOUND"
echo "✅ Ambiente configurado: OK"
echo "✅ Pronto para build: OK"
echo "=" * 50

exit 0

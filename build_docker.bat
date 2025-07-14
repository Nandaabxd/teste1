@echo off
echo.
echo 🐳 DOCKER BUILD - NFC Writer PRO v2.0
echo =====================================
echo 📱 Compilando APK com ambiente isolado...
echo.

REM Verifica se Docker está instalado
echo 🔍 Verificando Docker...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker não encontrado!
    echo.
    echo 📥 INSTALE DOCKER DESKTOP:
    echo    1. Acesse: https://www.docker.com/products/docker-desktop/
    echo    2. Baixe e instale
    echo    3. Reinicie o computador
    echo    4. Execute este script novamente
    echo.
    pause
    exit /b 1
)

echo ✅ Docker encontrado - OK
echo.

REM Mostra informações do sistema
echo 📊 Informações do Sistema:
echo    Docker ativo e funcionando
echo.

REM Limpa builds anteriores se solicitado
echo 🧹 Deseja limpar builds anteriores? (s/N)
set /p clean="> "
if /i "%clean%"=="s" (
    echo    Limpando imagens antigas...
    docker rmi nfc-app-builder 2>nul
    docker system prune -f >nul 2>&1
    echo    ✅ Limpeza concluída
    echo.
)

REM Constrói a imagem Docker
echo 🏗️  Construindo imagem Docker (pode demorar 10-15 min na primeira vez)...
echo    📦 Baixando Ubuntu 22.04...
echo    ☕ Instalando Java, Python, Android SDK/NDK...
echo    ⚙️  Configurando Buildozer...
echo.
docker build -t nfc-app-builder .

if %errorlevel% neq 0 (
    echo.
    echo ❌ ERRO ao construir imagem Docker
    echo.
    echo 🔧 SOLUÇÕES:
    echo    1. Verifique sua conexão com internet
    echo    2. Aumente memória do Docker (Settings ^> Resources ^> Memory: 6GB+)
    echo    3. Desative antivírus temporariamente
    echo    4. Execute: docker system prune -a -f
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Imagem Docker construída com sucesso!
echo.

REM Cria diretório bin se não existir
if not exist "bin" mkdir bin

REM Executa o container e compila o APK
echo 🔧 Iniciando compilação do APK...
echo    📱 App: NFC Writer PRO v2.0
echo    🎯 Target: Android API 33
echo    📐 Arch: ARM 32/64-bit
echo    ⏱️  Tempo estimado: 8-15 minutos
echo.
echo ⏳ Aguarde... (logs em tempo real)
echo.

docker run --rm -v "%cd%":/workspace nfc-app-builder

if %errorlevel% neq 0 (
    echo.
    echo ❌ ERRO durante compilação
    echo.
    echo 🔧 DIAGNÓSTICO:
    echo    1. Verificando logs...
    echo.
    echo 💡 SOLUÇÕES:
    echo    1. Execute novamente (builds subsequentes são mais rápidos)
    echo    2. Use build limpo: docker rmi nfc-app-builder
    echo    3. Verifique TUTORIAL_DOCKER.md para troubleshooting
    echo.
    pause
    exit /b 1
)

echo.
echo 🎉 COMPILAÇÃO CONCLUÍDA COM SUCESSO!
echo =====================================
echo.

REM Verifica se APK foi gerado
if exist "bin\*.apk" (
    echo ✅ APK gerado com sucesso!
    echo.
    echo 📁 Localização:
    for %%f in (bin\*.apk) do (
        echo    📱 %%f
        echo    📊 Tamanho: 
        dir "%%f" | findstr "%%~nxf"
    )
    echo.
    echo 🚀 PRÓXIMOS PASSOS:
    echo    1. 📲 Copie o APK para seu celular Android
    echo    2. ⚙️  Vá em Configurações ^> Segurança ^> Fontes Desconhecidas
    echo    3. 📱 Toque no APK para instalar
    echo    4. 🔍 Abra o app e teste com tags NFC
    echo.
    echo 💡 DICA: Aproxime uma tag NFC do celular para testar!
    echo.
    echo 🎯 APP INSTALADO: "NFC Reader PRO"
) else (
    echo ❌ APK não foi gerado
    echo.
    echo 🔍 VERIFICAÇÃO:
    echo    1. Logs acima mostram o erro
    echo    2. Consulte TUTORIAL_DOCKER.md para troubleshooting
    echo    3. Tente executar novamente
    echo.
)

echo.
echo 📚 Documentação completa: TUTORIAL_DOCKER.md
echo.
pause

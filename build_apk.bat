@echo off
echo ===================================================
echo    NFC Reader ^& Writer PRO - Build System
echo ===================================================

echo [1/6] Verificando ambiente...
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERRO: Python nao encontrado no PATH!
    echo Instale Python 3.9+ e adicione ao PATH
    pause
    exit /b 1
)

echo [2/6] Verificando buildozer...
pip show buildozer >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Instalando buildozer...
    pip install buildozer Cython==0.29.33
) else (
    echo Buildozer ja instalado.
)

echo [3/6] Limpando builds anteriores...
if exist .buildozer (
    echo Removendo cache antigo...
    rmdir /s /q .buildozer 2>nul
)
if exist bin (
    echo Limpando diretorio bin...
    rmdir /s /q bin 2>nul
)

echo [4/6] Verificando configuracao...
if not exist buildozer.spec (
    echo ERRO: buildozer.spec nao encontrado!
    pause
    exit /b 1
)

echo [5/6] Iniciando compilacao do APK...
echo AVISO: Este processo pode demorar 15-30 minutos na primeira vez
echo porque precisa baixar Android SDK, NDK e dependencias.
echo.
set /p choice="Continuar? (s/n): "
if /i not "%choice%"=="s" (
    echo Build cancelado pelo usuario.
    pause
    exit /b 0
)

echo.
echo Compilando... Por favor aguarde...
buildozer android debug

echo.
echo [6/6] Verificando resultado...
if exist bin\*.apk (
    echo.
    echo ===================================================
    echo              BUILD CONCLUIDO COM SUCESSO!
    echo ===================================================
    echo.
    for %%f in (bin\*.apk) do (
        echo APK gerado: %%f
        echo Tamanho: 
        dir /B %%f | findstr /C:"."
    )
    echo.
    echo Para instalar no dispositivo:
    echo 1. Conecte o dispositivo Android via USB
    echo 2. Ative "Depuracao USB" nas configuracoes
    echo 3. Execute: adb install bin\nfcwriterpro-2.0-debug.apk
    echo.
    echo Ou copie o arquivo APK para o dispositivo e instale manualmente.
    echo.
) else (
    echo.
    echo ===================================================
    echo                ERRO NO BUILD!
    echo ===================================================
    echo.
    echo Verifique as mensagens de erro acima.
    echo Problemas comuns:
    echo - Falta de espaco em disco
    echo - Problemas de conectividade
    echo - Versoes incompativeis de dependencias
    echo.
    echo Tente executar: buildozer android clean
    echo E depois rode este script novamente.
    echo.
)

pause

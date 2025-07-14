@echo off
echo ===============================================
echo    Monitor de Build - NFC Reader PRO
echo ===============================================
echo.

:monitor_loop
cls
echo ===============================================
echo    Monitor de Build - %TIME%
echo ===============================================
echo.

echo [STATUS DOS ARQUIVOS]
echo.

if exist .buildozer (
    echo ✓ Diretorio .buildozer: CRIADO
    if exist .buildozer\android (
        echo ✓ Platform Android: CONFIGURADO
    ) else (
        echo ⏳ Platform Android: PREPARANDO...
    )
) else (
    echo ⏳ Diretorio .buildozer: AGUARDANDO...
)

if exist bin (
    echo ✓ Diretorio bin: CRIADO
    for %%f in (bin\*.apk) do (
        echo ✓ APK GERADO: %%f
        echo   Tamanho: 
        dir /B %%f
    )
) else (
    echo ⏳ Diretorio bin: AGUARDANDO...
)

echo.
echo [PROGRESSO ESTIMADO]
if exist .buildozer\android\platform (
    if exist .buildozer\android\platform\android-sdk (
        echo ✓ Android SDK: BAIXADO
    ) else (
        echo ⏳ Android SDK: BAIXANDO... (10-15 min)
    )
    
    if exist .buildozer\android\platform\android-ndk (
        echo ✓ Android NDK: BAIXADO
    ) else (
        echo ⏳ Android NDK: BAIXANDO... (5-10 min)
    )
    
    if exist .buildozer\android\platform\build (
        echo ✓ Compilacao: EM ANDAMENTO
    ) else (
        echo ⏳ Compilacao: PREPARANDO...
    )
) else (
    echo ⏳ Preparando ambiente de build...
)

echo.
echo [LOGS RECENTES]
if exist .buildozer\android\platform\.buildozer.log (
    echo Ultimas linhas do log:
    powershell "Get-Content .buildozer\android\platform\.buildozer.log -Tail 3"
)

echo.
echo Pressione Ctrl+C para parar o monitor
echo Aguardando 30 segundos para proxima atualizacao...
echo.

timeout /t 30 /nobreak >nul 2>&1
goto monitor_loop

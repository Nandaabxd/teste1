@echo off
echo === Monitor de Compilacao APK ===
echo Verificando progresso da compilacao...
echo.

:LOOP
echo [%TIME%] Verificando status...
wsl -e bash -c "cd ~/nfc-app && ls -la bin/ 2>/dev/null || echo 'Pasta bin ainda nao criada'"
echo.
timeout /t 60 /nobreak >nul
goto LOOP

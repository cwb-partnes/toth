@echo off
title Servidor Toth Corretora
echo ==========================================
echo   Iniciando Servidor Local - Toth Corretora
echo ==========================================
echo.
echo Para acessar o site, use: http://localhost:8000
echo.
npx -y live-server . --port=8000 --no-browser
pause

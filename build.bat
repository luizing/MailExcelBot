@echo off
setlocal

rem Prompt para as credenciais
set /p user_email="Digite o email que servirá como bot: "
set /p user_pass="Digite a senha: "

rem Cria o arquivo config.ini
echo [credentials] > config.ini
echo email = %user_email% >> config.ini
echo password = %user_pass% >> config.ini

echo Arquivo config.ini criado com sucesso!

endlocal
pause

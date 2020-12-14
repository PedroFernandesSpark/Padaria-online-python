#!/bin/sh
sudo apt-get update
sudo apt-get install mysql-server
sudo apt install python3

python3 -m pip install -r PyDaria/requirements.txt

echo "Por favor altere a senha no arquivo database.py para que ele seja igual que voce cadastrou para o usuario root do mysql."
echo "Cuidado para nao alterar nada alem da senha!"
echo "Caminho do arquivo: PyDaria/PyDaria/backend/database.py"

chmod u+x execute.sh
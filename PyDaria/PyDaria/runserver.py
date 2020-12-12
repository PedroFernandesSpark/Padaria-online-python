"""@package docstring
Rode esse scrip para iniciar o server.
"""


"""
importações padrões para o funcionamento do servidor
"""
from os import environ
from PyDaria import app

"""
gera as portas e inicializa o servidor
"""
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

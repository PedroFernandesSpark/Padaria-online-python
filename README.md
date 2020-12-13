# Padaria-online-python
Trabalho final da disciplina métodos de programação, um sistema web feito em python


# Processo de execução do projeto em LINUX:
1- Clone o projeto em um repositório de sua escolha

2- Acesse a pasta PyDaria:
$ cd PyDaria

3- Dê permissão de execução para o script dependecies.sh:
$ chmod u+x dependecies.sh

4- Execute o comando:
$ ./dependecies.sh

5- Configure a senha do MySQL no arquivo database.py como descrito no final dessa página 

6- Execute o script execute.sh:
$ ./execute.sh

7- Acesse o link no terminal ou va até:
http://localhost:5555/

# Processo de execução do projeto em WINDOWS 10:
1- Baixe o compilador de python (versão 3 ou superior) pelo site https://www.python.org/downloads/ na opção "Download windows", 

2- Baixe o pip via cmd seguindo as instruções oficiais em https://pip.pypa.io/en/stable/installing/ (selecione a opção para windows)


3-Baixe o FLASK seguindo as informações oficiais em https://flask.palletsprojects.com/en/1.1.x/installation/

4- Agora que você já tem todos os recursos necessários, clone ou faça o download do projeto e localize-o em seu computador.
Navegue até o mesmo por meio do comando:
$ cd endereço-do-diretorio

5- É necessário navegar agora até um diretório mais interno do sistema. Seu endereço agora deve se parecer com .../Padaria-online-python
Via cmd, utilize o seguinte comando:
$ cd PyDaria/PyDaria

6- Siga os passos descritos no final da página para configurar o MySQL

7- Execute os scritps database.py e populate_tables.py:
$ python backend/database.py
$ python backend/populate_tables.py

7- Agora que estamos no diretório final, bastam 2 comandos para rodar o servidor do projeto localmente.
Utilize, via cmd, os seguintes comandos:
verifique que está em um diretorio como <alguma-coisa/PyDaria/PyDaria>
então rode o comando :
$ py -3 runserver.py 

8- Agora, com seu servidor funcionando, abra o Google Chrome do seu computador (mozilla Firefox não reconhece alguns artefatos visuais implementados) e navegue até o endereço 
http://127.0.0.1:5000/


# Configurando o MySQL e o banco de dados
1- Se você rodou o script do linux você ja deve ter tudo necessário instalado, se você estiver no Windows instale o MySQL workbench disponível em:
https://dev.mysql.com/downloads/workbench/

2- Configure o MySQL. É crucial que o tipo de autenticação seja mysql_native_password para que o sistema funcione devidamente

3- Acesse a pasta backend e altere a senha do usuário root para a que você cadastrou no MySQL. Caminho do arquivo:
Pydaria/PyDaria/backend/database.py

# Informações
A navegação do site é como a de qualquer outro site conhecido na internet, com algumas considerações:
 
 1- Não foi implementado um sistema de entregas pois é suposto que o cliente usaria o site para apenas fazer reservas de produtos na PyDaria física.
 
 2- Os produtos são todos comprados por quantidade de unidades, e não por peso ou volume.
 
 

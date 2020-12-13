# Padaria-online-python
Trabalho final da disciplina métodos de programação, um sistema web feito em python


# Processo de execução do projeto em LINUX:
1- Baixe o compilador de python via terminal:
$ sudo apt-get install python3

2- Baixe o pip via terminal:
$ sudo apt install python3-pip

3-Baixe o FLASK via terminal:
$ pip install -U Flask

4- Agora que você já tem todos os recursos necessários, faça download do projeto e localize-o em seu computador.
Navegue até o mesmo por meio do comando:
$ cd endereço-do-diretorio

5- É necessário navegar agora até um diretório mais interno do sistema. Seu endereço agora deve se parecer com .../Padaria-online-python
Via terminal, utilize o seguinte comando:
$ cd PyDaria/PyDaria

6- Agora que estamos no diretório final, bastam 2 comandos para rodar o servidor do projeto localmente.
Utilize, via terminal, os seguintes comandos:
$ export FLASK_APP=runserver.py
$ flask run

7- Agora, com seu servidor funcionando, abra o Google Chrome do seu computador (mozilla Firefox não reconhece alguns artefatos visuais implementados) e navegue até o endereço 
http://127.0.0.1:5000/

A navegação do site é como a de qualquer outro site conhecido na internet, com algumas considerações:

1- Os produtos inicialmente mostrados são apenas visuais, sem recursos funcionais.
   Para isto, é necessário criar uma conta com o CPF 12345678900 e fazer login. Isso o redirecionará a uma página de criação de produtos.
   Preencha os campos presentes com os dados que quiser.
   Obs.: as imagens do projeto estão no diretório de endereço /Padaria-online-python/PyDaria/PyDaria/PyDaria/staitc/img
 
 2- Não foi implementado um sistema de entregas pois é suposto que o cliente usaria o site para apenas fazer reservas de produtos na PyDaria física.
 
 3- Os produtos são todos comprados por quantidade de unidades, e não por peso ou volume.

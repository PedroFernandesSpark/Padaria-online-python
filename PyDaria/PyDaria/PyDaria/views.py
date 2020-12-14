# -*- coding: utf-8 -*-

"""@package docstring
Esse arquivo comanda as rotas e suas lógicas de funcionamento basicas.
"""

"""
Importação da biblioteca de:
tempo e data,
flask padrão,
app,
banco de dados
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for, session
from PyDaria import app
from backend.database import show_client, add_client, add_product, rmv_product, show_all_products, show_product, add_to_cart, show_cart, show_cart_val, rmv_from_cart

"""
Definição das funções do database.py:

add_client(cpf, name, email, telephone, password)

show_client(cpf) return: ((id, name, email, telephone, cpf, isAdmin, password))

add_product(name, price, img, qtd, description)

rmv_product(id_produto)

show_all_products() return: ((id, price, name, img, qtd, description), (id, price, ...), ...)

show_product(id_produto) return: ((id, price, name, img, qtd, description))

add_to_cart(cpf, id_produto, quantidade)

show_cart(cpf) return: ((cpf, qtd, id_produto, preco_unitario, preco_total), (cpf, qtd, ...), ...)

show_cart_val(cpf) return: int valor total

rmv_from_cart(cpf, id_produto)
"""

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
NOME_CLIENTE = 'Nome do cliente'
CLIENT_NOT_FOUND = 'Cliente não encontrado'
CLIENT_NOT_LOGGED = 'Por favor, faça login'
CPF_ALREADY_REGISTERED = 'Já tem um usuário cadastrado com esse CPF'
WRONG_CPF = 'CPF Incorreto'
WRONG_PASSWORD = 'Senha Incorreta'
PRODUCT_NOT_FOUND = 'Produto Inexistente'
QUANTITY_NOT_POSITIVE = 'Coloque pelo menos um item no carrinho!'
PRODUCT_UNAVAILABLE = 'Produto Indisponível'
NO_SUFFICIENT_PRODUCT = 'Só tem {} desse produto no estoque'

@app.route('/')
@app.route('/home')
def home():
    """
    Função: Renderizar a home page

    Descrição: Caso a rota seja baseURL + / ou /home, ela verifica se o usuario esta logado, 
    pega o nome do usuario (caso logado), da set na session para menter o usuario logado no site, 
    retorna o HTML da pagina.

    Valor retornado: um arquivo html renderizado referente a pagina index.
    Assertiva de Saida: será renderizaro um arquivo html da página index com as informações de nome, 
    titulo da pagina e se o usuario está ou não logado.
    """
    logado = False
    nome = NOME_CLIENTE
    admin = False
    produtos = show_all_products()
    if session and session['client_cpf']:
        """
        verifica se existe uma sessão e se ela possui um cpf
        """
        logado = True
        client = show_client(session['client_cpf'])
        if not client:
            """
            Se o cliente não existir, nome fica como 'cliente não encontrado'
            """
            nome = CLIENT_NOT_FOUND
        else:
            """
            Se não, ele atribui ao nome o nome do cliente que vem como client[0][1]
            """
            nome = client[0][1]
            if client[0][4] == "12345678900" or client[0][4] == "112233445566":
                """
                    Checa se o usuário é admin, se for, manda essa informação para o site
                """
                admin = True
    return render_template(
        'index.html',
        title='Home Page',
        logado=logado,
        nome=nome,
        admin=admin,
        produtos=produtos,
        year=datetime.now().year,
    )
    """
    Renderiza o template
    """

@app.route('/signin', methods=['GET', 'POST'])
def singup():
    """
    Função: Renderizar a pagina de cadastro

    Descrição: Caso a rota seja baseURL + /signin, ela, no get, set os valores de cpf, nome, email, telefone e senha, então
    passa, por meio de uma post, os valores para o banco de dados, caso o cpf não exista no banco de dados.

    Valor retornado: um arquivo html renderizado referente a pagina signin.

    Assertiva de entrada: aceita os metodos post e get.

    Assertiva de Saida: Se o metodo for get será renderizaro um arquivo html da página signin com as informações de erro, 
    titulo da pagina e data
    Se não, ela retorna um redirect para a home page.
    """
    error = None
    if request.method == 'POST' and request.form:
        """
        verifica se o metodo é post e se o formulario foi preenchido
        """
        cpf = request.form['cpf']
        if show_client(cpf):
            """
            Verifica a duplicidade do cpf informado, dando uma mensagem de erro caso ele já exista.
            """
            error = CPF_ALREADY_REGISTERED
        name = request.form['name']
        email = request.form['email']
        telephone = request.form['phone']
        password = request.form['password']
        if not error:
            """
            Verifica se não há erros.
            """    
            add_client(cpf,name,email,telephone,password)
            return redirect(url_for('login'))
    if session and session['client_cpf']:
        """
        Verifica se já existe uma sessão atual.
        """
        return redirect(url_for('home'))
    return render_template(
        'signin.html',
        title='PyDaria',
        year=datetime.now().year,
        error=error,
        message='Your contact page.'
    )

@app.route('/login', methods=['GET','POST'])
def login():
    """
    Função: Renderizar a login page

    Descrição: Caso a rota seja baseURL + /login,  ela, no get, set os valores de cpf e senha, então
    verifica, por meio de uma post, se os valores de cpf e senha estão corretos para um mesmo usuario e set seu login.

    Valor retornado: um arquivo html renderizado referente a pagina login.

    Assertiva de entrada: aceita os metodos post e get.

    Assertiva de Saida: Se o metodo for get será renderizaro um arquivo html da página login com as informações de erro, 
    titulo da pagina, mensagem e data
    Se não, ela retorna um redirect para a home page e set o login.
    """
    error = None
    if request.method == 'POST' and request.form:
        """
        verifica se o metodo é post e se o formulario foi preenchido
        """
        cpf = request.form['cpf']
        password = request.form['password']
        client = show_client(cpf)
        if not client:
            """
            Verifica se existe aquele cpf no banco de dados
            """
            error = WRONG_CPF
        elif password != client[0][6]:
            """
            Verifica se a senha é igual a do banco de dados.
            """
            error = WRONG_PASSWORD
        if error is None:
            """
            Verifica se há erros
            """
            session.clear()
            session['client_cpf'] = client[0][4]
            session.permanent = True
            session.permanent_session_lifetime = 36000
            if client[0][4] == "12345678900" or client[0][4] == "112233445566":
                """
                Verifica se as informações de login são as do admin.
                """
                """
                Caso o user seja o admin, retorna redirect para o backlog.
                """
                return redirect(url_for('productadm'))
            """
            Caso não, retorna para a home page.
            """
            return redirect(url_for('home'))
    if session and session['client_cpf']:
        """
        Verifica se o usuario já está logado e o retorna para a home page.
        """
        return redirect(url_for('home'))
    """
    Retorna o rendere da login page.
    """
    return render_template(
        'login.html',
        title='PyDaria',
        year=datetime.now().year,
        message='Your contact page.',
        error=error
    )

@app.route('/backoffice/produtos')
def productadm():
    """
    Função: Renderizar a pagina de administração dos produtos

    Descrição: Caso a rota seja baseURL + /backoffice/produtos,  ela renderiza um html com uma tabela listando todos os produtos,
    com seus valores do banco de dados, com link para a criação de novos produtos, edição dos existentes ou delete dos mesmos.

    Valor retornado: um arquivo html renderizado referente a pagina backoffice_produtos.

    Assertiva de entrada: aceita o metodo get.

    Assertiva de Saida: Se o metodo for get será renderizaro um arquivo html da página backoffice de produtos
    """
    logado = False
    nome = NOME_CLIENTE
    if session and session['client_cpf']:

        """
        Verfica se o usuario esta logado.
        """
        logado = True
        client = show_client(session['client_cpf'])
        if not client:
            """
            Verifica se a sessão possui um valor de cpf
            """
            nome = CLIENT_NOT_FOUND
        else:
            if client[0][4] != "12345678900" and client[0][4] != "112233445566":
                """
                verifica se o cliente não é admin.
                """
                """
                Retorna um redirect para a home page caso o user não seja admin.
                """
                return redirect(url_for('home'))
            nome = client[0][1]
    """
    Retorna o render da pagina.
    """
    produtos = show_all_products()
    return render_template(
        'backoffice_product.html',
        title='Backoffice dos produtos',
        logado = logado,
        produtos=produtos,
        nome = nome,
        year=datetime.now().year,
    )

@app.route('/backoffice/produtos/create', methods=['GET','POST'])
def productcreate():
    """
    Função: Renderizar a pagina de criação de produtos

    Descrição: Caso a rota seja baseURL + /backoffice/produtos/create, caso Get  ela renderiza um html com uma formulario do produto,
    caso Post ele insere as informações no banco de dados.

    Valor retornado: um arquivo html renderizado referente a pagina backoffice_produtos.

    Assertiva de entrada: aceita o metodo get e post.

    Assertiva de Saida: Se o metodo for get será renderizaro um arquivo html da página backoffice de produtos,
    se for post ele insere no banco de dados os valores passados no body do post.
    """
    if request.method == 'POST' and request.form:
        """
        Verifica se o metodo é post.
        """
        name = request.form['nome_produto']
        price = request.form['preco']
        if "," in price:
            price = price.replace(",", ".")
        price = float(price)
        img = request.form['image']
        qtd = request.form['stock']
        desc = request.form['descricao']
        if not desc:
            desc = "Sem Descrição"
        add_product(name, price, img, qtd, desc)
        """
        redireciona para a pagina de administração dos produtos.
        """
        return redirect(url_for("productadm"))
    else:
        """
        Caso o metodo não seja post. (logo ele sera get).
        """
        logado = False
        nome = NOME_CLIENTE
        if session and session['client_cpf']:
            """
            Verifica se o user esta logado.
            """
            logado = True
            client = show_client(session['client_cpf'])
            if client[0][4] != "12345678900" and client[0][4] != "112233445566":
                """
                Verifica se o user não é admin.
                """
                """
                Retorna o redirect para a home page caso o user n seja o admin.
                """
                return redirect(url_for('home'))
            nome = client[0][1]
            if not client:
                """
                Verifica se o cpf esta presente na session.
                """
                nome = CLIENT_NOT_FOUND
        """
        Retorna o render da pagina.
        """
        return render_template(
            'backoffice_product_create.html',
            title='Backoffice dos produtos',
            logado = logado,
            nome = nome,
            year=datetime.now().year,
        )

@app.route('/backoffice/produtos/remove/<prod_id>')
def remove_product(prod_id):
    if session and session['client_cpf'] and (session['client_cpf'] == "12345678900" or session['client_cpf'] == "112233445566"):
        produto = show_product(prod_id)
        if produto:
            rmv_product(prod_id)
        return redirect(url_for("productadm"))
    return redirect(url_for("home"))

@app.route('/prod/<prod_id>', methods=['GET','POST'])
def produto(prod_id):
    """
    Função: Renderizar a pagina de produto.

    Descrição: Caso a rota seja baseURL + /prod/<prod_id> renderiza o html do produto com prod_id e da a opção para adicionar o produto ao carrinho.

    Valor retornado: renderiza o html da pagina do produto selecionado.

    Assertiva de entrada: aceita o metodo get e post.

    Assertiva de Saida: renderiza um html para o produto selecionado.
    """
    error = None
    logado = False
    nome = NOME_CLIENTE
    produto = show_product(prod_id)
    if not produto or not produto[0]:
        error=PRODUCT_NOT_FOUND
    else:
        produto = produto[0]
    if session and session['client_cpf']:
        """
        Verifica se o user esta logado.
        """
        logado = True
        client = show_client(session['client_cpf'])
        if not client:
            """
            Verifica se o cpf esta presente na session.
            """
            nome = CLIENT_NOT_FOUND
        else:
            nome = client[0][1]
    """
    Retorna o render da pagina.
    """
    return render_template(
        'produto.html',
        logado=logado,
        nome=nome,
        produto=produto,
        error=error
    )

@app.route('/prod/<prod_id>/add', methods=['POST'])
def add_produto(prod_id):
    """
    Função: Adicionar o produto com id prod_id ao carrinho.

    Descrição: Caso a rota seja baseURL + /prod/<prod_id>/add adiciona o produto ao carrinho com o cpf do cliente, id do produto e quantidade.

    Valor retornado: retorna para a página index para o cliente comprar mais produtos.

    Assertiva de entrada: aceita o metodo post, id_prod tem um produto no banco de dados correspondente, o usuário está logado e a quantidade é maior do que 1.

    Assertiva de Saida: adiciona o cpf, o prod_id e a quantidade no banco de dados do carrinho.
    """
    error = None
    produto = show_product(prod_id)
    produto = produto[0]
    if produto and request.method == "POST" and request.form:
        """
        verifica se o produto e request.form existem e se o metodo é post
        """
        quantidade = int(request.form['quantidade'])
        if int(quantidade) <= 0:
            """
            verifica se a quantidade é menor ou igual a zero
            """
            error = QUANTITY_NOT_POSITIVE
        elif produto[4] <= 0:
            """
            verifica se a produto[4] é menor ou igual a zero
            """
            error = error = PRODUCT_UNAVAILABLE
        elif produto[4] < quantidade:
            """
            verifica se a quantidade é maior que o estoque(produto[4])
            """
            error = NO_SUFFICIENT_PRODUCT.format(produto[4])
        elif not session or not session["client_cpf"]:
            """
            verifica se esta logado.
            """
            error = CLIENT_NOT_LOGGED
        else:
            carrinho = show_cart(session['client_cpf'])
            for produto in carrinho:
                """
                percorre o carrinho colocando cada valor na variavel temporaria 'produto'
                """
                if produto[2] == int(prod_id) and produto[0] == session['client_cpf']:
                    quantidade = quantidade + produto[1]
                    rmv_from_cart(session['client_cpf'], int(prod_id))
                    break
            add_to_cart(session["client_cpf"], prod_id, quantidade)
            """
            redireciona para a pagina do carrinho
            """
            return redirect(url_for('carrinho'))
    else:
        error = PRODUCT_NOT_FOUND
    logado = False
    nome = NOME_CLIENTE
    produto = show_product(prod_id)
    if not produto or not produto[0]:
        error=PRODUCT_NOT_FOUND
    else:
        produto = produto[0]
    if session and session['client_cpf']:
        """
        Verifica se o user esta logado.
        """
        logado = True
        client = show_client(session['client_cpf'])
        if not client:
            """
            Verifica se o cpf esta presente na session.
            """
            nome = CLIENT_NOT_FOUND
        else:
            nome = client[0][1]
    return render_template(
        'produto.html',
        logado=logado,
        nome=nome,
        produto=produto,
        error=error
    )

@app.route('/carrinho', methods=['GET','POST'])
def carrinho():
    """
    Função: Renderizar a pagina do carrinho.

    Descrição: Caso a rota seja baseURL + /carrinho renderiza o html do carrinho e da a opção de finalizar compra.

    Valor retornado: renderiza o html da pagina do carrinho.

    Assertiva de entrada: aceita o metodo get e post.

    Assertiva de Saida: renderiza um html para o carrinho.
    """
    logado = False
    nome = NOME_CLIENTE
    carrinho = None
    total = None
    admin = False
    produtos = {}
    if session and session['client_cpf']:
        """
        Verifica se o usuario esta logado.
        """
        logado = True
        client = show_client(session['client_cpf'])
        if not client:
            nome = CLIENT_NOT_FOUND
        else:
            nome = client[0][1]
        if client[0][4] == "12345678900" or client[0][4] == "112233445566":
            """
                Checa se o usuário é admin, se for, manda essa informação para o site
            """
            admin = True
    if logado:
        """
        verifica se esta logado.
        """
        carrinho = show_cart(session['client_cpf'])
        for produto in carrinho:
            """
            percorre o carrinho colocando cada item na variavel temporaria 'produto'
            """
            produtos[produto[2]] = show_product(produto[2])[0]
        total = show_cart_val(session['client_cpf'])
    """
    Retorna o render da pagina.
    """
    return render_template(
        'carrinho.html',
        logado=logado,
        nome=nome,
        admin=admin,
        carrinho=carrinho,
        produtos=produtos,
        total=total
    )

@app.route('/cart/delete/<prod_id>')
def delete_from_cart(prod_id):
    """
    Função: Deleta um item do carrinho.

    Descrição: Caso a rota seja baseURL + //cart/delete/<prod_id> ele exclui do carrinho do user o item com o id informado na requisição

    Valor retornado: Deleta o item do carrinho.

    Assertiva de entrada: aceita o metodo get e o valor id do item a ser deletado.

    Assertiva de Saida: Deleta o item do carrinho.
    """
    if session and session['client_cpf']:
        """
        verifica se o user esta logado.
        """
        carrinho = show_cart(session['client_cpf'])
        for produto in carrinho:
            """
            passa pelos itens dentro do carrinho, atribuindo o valor de cada item 
            na variavel temporaria 'produto'
            """
            if produto[2] == int(prod_id):
                """
                verifica o valor 2 (id) de cada item do carrinho é igual ao id adicionado.
                """
                rmv_from_cart(session['client_cpf'], int(prod_id))
                """
                redireciona o usuer para o carrinho apos apagar o item escolhido
                """
                return redirect(url_for('carrinho'))
        return redirect(url_for('carrinho'))
    else:
        """
        caso falhe, retorna o user para a home page.
        """
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    """
    Função: Deslogar o atual cliente logado na session.

    Descrição: Caso a rota seja baseURL + /logout ele desloga o cliente limpando a session.

    Valor retornado: um redirect para a pagina principal.

    Assertiva de entrada: aceita o metodo get.

    Assertiva de Saida: Limpa session e redireciona para a home page.
    """
    session.clear()
    """
    Redireciona para a home page.
    """
    return redirect(url_for('home'))
# -*- coding: utf-8 -*-

"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for, session
from PyDaria import app
from backend.database import show_client, add_client, add_product, show_all_products, show_product, add_to_cart

# Definições das funções do database.py:

# add_client(cpf, name, email, telephone, password)

# show_client(cpf) return: ((id, name, email, telephone, cpf, isAdmin, password))

# add_product(name, price, img, qtd, description)

# show_all_products()

# show_product(id_produto)

# add_to_cart(cpf, id_produto, quantidade)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
NOME_CLIENTE = 'Nome do cliente'
CLIENT_NOT_FOUND = 'Cliente não encontrado'

@app.route('/')
@app.route('/home')
def home():
    "this will render the home page"
    logado = False
    nome = NOME_CLIENTE
    admin = False
    produtos = show_all_products()
    if session and session['client_cpf']:
        logado = True
        client = show_client(session['client_cpf'])
        if not client:
            nome = CLIENT_NOT_FOUND
        else:
            nome = client[0][1]
        if client[0][4] == "12345678900" or client[0][4] == "112233445566":
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

@app.route('/signin', methods=['GET', 'POST'])
def singup():
    error = None
    if request.method == 'POST' and request.form:
        cpf = request.form['cpf']
        if show_client(cpf):
            error = "Já tem um usuário cadastrado com esse CPF"
        name = request.form['name']
        email = request.form['email']
        telephone = request.form['phone']
        password = request.form['password']
        if not error:    
            add_client(cpf,name,email,telephone,password)
            return redirect(url_for('login'))
    if session and session['client_cpf']:
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
    error = None
    if request.method == 'POST' and request.form:
        cpf = request.form['cpf']
        password = request.form['password']
        client = show_client(cpf)
        if not client:
            error = "CPF Incorreto"
        elif password != client[0][6]:
            error = "Senha Incorreta"
        if error is None:
            session.clear()
            session['client_cpf'] = client[0][4]
            session.permanent = True
            session.permanent_session_lifetime = 36000
            if client[0][4] == "12345678900" or client[0][4] == "112233445566":
                return redirect(url_for('productadm'))
            return redirect(url_for('home'))
    if session and session['client_cpf']:
        return redirect(url_for('home'))
    return render_template(
        'login.html',
        title='PyDaria',
        year=datetime.now().year,
        message='Your contact page.',
        error=error
    )

@app.route('/backoffice/produtos')
def productadm():
    logado = False
    nome = NOME_CLIENTE
    if session and session['client_cpf']:
        logado = True
        client = show_client(session['client_cpf'])
        if not client:
            nome = CLIENT_NOT_FOUND
        else:
            if client[0][4] != "12345678900" and client[0][4] != "112233445566":
                return redirect(url_for('home'))
            nome = client[0][1]
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
    if request.method == 'POST' and request.form:
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
        return redirect(url_for("productadm"))
    else:
        logado = False
        nome = NOME_CLIENTE
        if session and session['client_cpf']:
            logado = True
            client = show_client(session['client_cpf'])
            if client[0][4] != "12345678900" and client[0][4] != "112233445566":
                return redirect(url_for('home'))
            nome = client[0][1]
            if not client:
                nome = CLIENT_NOT_FOUND
        return render_template(
            'backoffice_product_create.html',
            title='Backoffice dos produtos',
            logado = logado,
            nome = nome,
            year=datetime.now().year,
        )

@app.route('/prod/<prod_id>', methods=['GET','POST'])
def produto(prod_id):
    logado = False
    nome = NOME_CLIENTE
    error = None
    produto = show_product(prod_id)
    if not produto or not produto[0]:
        error="Produto Inexistente"
    else:
        produto = produto[0]
    if session and session['client_cpf']:
        logado = True
        client = show_client(session['client_cpf'])
        if not client:
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
    logado = False
    nome = NOME_CLIENTE
    if session and session['client_cpf']:
        logado = True
        client = show_client(session['client_cpf'])
        if not client:
            nome = CLIENT_NOT_FOUND
        else:
            nome = client[0][1]
    return render_template(
        'carrinho.html',
        logado=logado,
        nome=nome,
        carrinho=carrinho
    )

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
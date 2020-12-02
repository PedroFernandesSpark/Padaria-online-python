# -*- coding: utf-8 -*-

"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from PyDaria import app
import backend.database


logado = False
nome = 'Nome do cliente'

@app.route('/')
@app.route('/home')
def home():
    "this will render the home page"
    return render_template(
        'index.html',
        title='Home Page',
        logado=logado,
        nome=nome,
        year=datetime.now().year,
    )

@app.route('/signin', methods=['GET', 'POST'])
def singup():
    if request.method == 'POST' & request.form:
        cpf = request.form['cpf']
        name = request.form['name']
        name = request.form['email']
        telephone = request.form['phone']
        password = request.form['password']
        database.add_client(cpf,name,email.telephone,password)
    else:
        return render_template(
            'signin.html',
            title='PyDaria',
            year=datetime.now().year,
            message='Your contact page.'
        )

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['CPF'] != '12345678900' or request.form['Senha'] != '1234':   
            error = 'Erro. Usuario nao identificado.'
        else:
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
    return render_template(
        'backoffice_product.html',
        title='Backoffice dos produtos',
        year=datetime.now().year,
    )

@app.route('/backoffice/produtos/create', methods=['GET','POST'])
def productcreate():
    if request.method = 'POST':
        name = request.form['nome_produto']
        descricao = request.form['descricao']
        img = request.form['image']
        qtd = request.form['stock']
        database.add_product(name, price, img, qtd)
    else:
        return render_template(
            'backoffice_product_create.html',
            title='Backoffice dos produtos',
            year=datetime.now().year,
        )

@app.route('/produto', methods=['GET','POST'])
def produto():
    #logado = False
    #nome = 'Nome Do Cliente'
    return render_template(
    'produto.html',
    logado=logado,
    nome=nome,
    produto=produto
    )
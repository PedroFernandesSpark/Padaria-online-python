# -*- coding: utf-8 -*-

"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from PyDaria import app

@app.route('/')
@app.route('/home')
def home():
    "this will render the home page"
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/signin', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return request.form
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

@app.route('/backoffice/produtos/create')
def productcreate():
    return render_template(
        'backoffice_product_create.html',
        title='Backoffice dos produtos',
        year=datetime.now().year,
    )
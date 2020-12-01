# -*- coding: utf-8 -*-

"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for, session
from PyDaria import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    if 'cpf' in session:
        return render_template(
        'index.html',
        title='Home Page',
        client=session['cpf'],
        year=datetime.now().year,
    )
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/signin', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cpf = request.form['cpf']
        phone = request.form['phone']
        password = request.form['password']
        if not name:
            error = "Name is required"
        elif not email:
            error = "Email is required"
        elif not cpf:
            error = "CPF is required"
        elif not phone:
            error = "Phone is required"
        elif not password:
            error = "Password is required"
        elif db.execute(
            'SELECT id FROM clients WHERE cpf = ?', (cpf,)
        ).fetchone() is not None:
            error = 'User cpf {} is already registered.'.format(cpf)

        if error is None:
            db.execute(
                'INSERT INTO clients (cpf, name, email, phone, password) VALUES (?, ?, ?, ?, ?)',
                (cpf, name, email, phone, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for(login))
        flash(error)
    else:
        return render_template(
            'signin.jade',
            title='PyDaria',
            year=datetime.now().year,
            message='Your contact page.'
        )

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        password = request.form['password']
        db = get_bd()
        error = None
        client = db.execute(
            'SELECT * FROM clients WHERE cpf = ?', (cpf,)
        ).fetchone()
        if user is None:
            error = 'Incorrect cpf'
        elif not check_password_hash(user['password'], password)
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['client_id'] = client['id']
            if client['cpf'] == '12345678900':
                return redirect(url_for('productadm')) 
            else:
                return redirect(url_for('home'))
        flash(error)
    return render_template(
    'login.html',
    title='PyDaria',
    year=datetime.now().year,
    message='Your contact page.',
    error=error
    )


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
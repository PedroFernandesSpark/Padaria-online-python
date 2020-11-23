"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from PyDaria import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.jade',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/signin', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "teste"
    else:
        return render_template(
            'signin.html',
            title='PyDaria',
            year=datetime.now().year,
            message='Your contact page.'
        )


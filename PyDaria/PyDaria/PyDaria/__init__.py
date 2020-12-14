"""
aplicação base do flask.
"""

from flask import Flask
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

import PyDaria.views

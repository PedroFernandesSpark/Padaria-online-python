from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////clients.db'
db = SQLAlchemy(app)

# Define a class for the Artist table
class Clients(db.Model):
    cpf = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    telefone = db.Column(db.String)

# Create the table
db.create_all()

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

# Create data abstraction layer
class ClientSchema(Schema):
    class Meta:
        type_ = 'client'
        self_view = 'client_one'
        self_view_kwargs = {'cpf': '<cpf>'}
        self_view_many = 'client_many'

    cpf = fields.Str()
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    telefone = fields.Str(required=True)

from flask_rest_jsonapi import Api, ResourceDetail, ResourceList

class ClientMany(ResourceList):
    schema = ClientSchema
    data_layer = {'session': db.session,
                  'model': Clients}

class ClientOne(ResourceDetail):
    schema = ClientSchema
    data_layer = {'session': db.session,
                  'model': Clients}

api = Api(app)
api.route(ClientMany, 'client_many', '/clients')
api.route(ClientOne, 'client_one', '/clients/<str:cpf>')

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.store import StoreList, Store
from resources.item import ItemList, Item
from resources.user import UserRegister
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROGATE_EXCEPTIONS'] = True
app.secret_key = 'mehdi_dev2021'

api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity)



api.add_resource(Store,'/store/<string:name>')
api.add_resource(Store,'/store')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)


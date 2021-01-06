from flask import Flask, request
from Item import Item
from User import User
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/item/add', methods=['POST'])
def add_item():
    item_session = Item('main.db')
    req_data = request.get_json()
    user_id = req_data['user_id']
    item_name = req_data['item_name']
    item_id = item_session.create(user_id, item_name)
    return {'user_id': user_id, 'item_id': item_id}, 201


@app.route('/user/add', methods=['POST'])
def add_user():
    user_session = User('main.db')
    req_data = request.get_json()
    user_name = req_data['user_name']
    user_id = user_session.create(user_name)
    return {'user_id': user_id}


@app.route('/user/get_items', methods=['GET'])
def get_user_items():
    item_session = Item('main.db')
    req_data = request.get_json()
    user_id = req_data['user_id']
    items = item_session.get_items(user_id)
    return {'items': items}


if __name__ == '__main__':
    app.run()

from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Menu, drink_schema, drinks_schema


api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
def getdata():
    return {'Hello': 'There'}

@api.route('/menu', methods = ['POST'])
@token_required
def add_drink(current_user_token):
    drink = Menu.query.get(id) 
    drink.drink_type = request.json['drink_type']
    drink.drink_name = request.json['drink_name']
    drink.flavor = request.json['flavor']
    drink.user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    drink = Menu(drink_type, drink_name, flavor, user_token = user_token )

    db.session.add(drink)
    db.session.commit()

    response = drink_schema.dump(drink)
    return jsonify(response)

@api.route('/menu', methods = ['GET'])
@token_required
def get_contact(current_user_token):
    a_user = current_user_token.token
    drinks = Menu.query.filter_by(user_token = a_user).all()
    response = drinks_schema.dump(drinks)
    return jsonify(response)

@api.route('/menu/<id>', methods = ['GET'])
@token_required
def get_single_car(current_user_token, id):
    drink = Menu.query.get(id)
    response = drink_schema.dump(drink)
    return jsonify(response)

@api.route('/menu/<id>', methods = ['POST','PUT'])
@token_required
def update_drink(current_user_token,id):
    drink = Menu.query.get(id) 
    drink.drink_type = request.json['drink_type']
    drink.drink_name = request.json['drink_name']
    drink.flavor = request.json['flavor']
    drink.user_token = current_user_token.token

    db.session.commit()
    response = drink_schema.dump(drink)
    return jsonify(response)

@api.route('/drink/<id>', methods = ['DELETE'])
@token_required
def delete_drink(current_user_token, id):
    drink = Menu.query.get(id)
    db.session.delete(drink)
    db.session.commit()
    response = drink_schema.dump(drink)
    return jsonify(response)
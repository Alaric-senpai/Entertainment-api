from flask import Blueprint, request, jsonify
from models import db, User, FavouriteShow, WatchList, UserDetails
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

api_bp = Blueprint('api', __name__)

@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password,
        usertype=data['usertype']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'})

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        token = str(uuid.uuid4())
        user.token = token
        db.session.commit()
        return jsonify({'message': 'Login successful', 'token': token})
    return jsonify({'message': 'Invalid credentials!'})

@api_bp.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found!'})
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'usertype': user.usertype,
        'token': user.token
    }
    return jsonify(user_data)

@api_bp.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found!'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User {id} deleted successfully!'})

@api_bp.route('/user/delete', methods=['DELETE'])
def delete_user_by_email():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        return jsonify({'message': 'User not found!'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User with email {data["email"]} deleted successfully!'})

@api_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'usertype': user.usertype,
            'token': user.token
        }
        user_list.append(user_data)
    return jsonify(user_list)

@api_bp.route('/favourites', methods=['POST'])
def add_favourite():
    data = request.get_json()
    new_favourite = FavouriteShow(
        useremail=data['useremail'],
        showid=data['showid'],
        addeddate=data['addeddate'],
        status=data['status']
    )
    db.session.add(new_favourite)
    db.session.commit()
    return jsonify({'message': 'Show added to favourites!'})

@api_bp.route('/watchlist', methods=['POST'])
def add_to_watchlist():
    data = request.get_json()
    new_watchlist = WatchList(
        useremail=data['useremail'],
        showid=data['showid'],
        addeddate=data['addeddate'],
        status=data['status']
    )
    db.session.add(new_watchlist)
    db.session.commit()
    return jsonify({'message': 'Show added to watchlist!'})

@api_bp.route('/userdetails/<id>', methods=['GET'])
def get_userdetails(id):
    userdetails = UserDetails.query.filter_by(user_id=id).first()
    if not userdetails:
        return jsonify({'message': 'User details not found!'})
    return jsonify({'bio': userdetails.bio})

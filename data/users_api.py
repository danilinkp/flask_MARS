import flask
from flask import jsonify, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'users': user.to_dict(only=('surname', 'name', 'age', 'address', 'email', 'position', 'speciality'))
        }
    )


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('surname', 'name', 'age', 'address', 'email', 'position', 'speciality'))
                 for item in users]
        }
    )


@blueprint.route('/api/user', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'address', 'email', 'position', 'speciality']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if request.json['id'] in [user.id for user in db_sess.query(User).all()]:
        return jsonify({'error': 'Id already exists'})
    db_sess = db_session.create_session()
    users = User(
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        address=request.json['address'],
        email=request.json['email'],
        speciality=request.json['speciality']
    )
    db_sess.add(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(user_id)
    if not users:
        return jsonify({'error': 'Not found'})
    db_sess.delete(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['PUT'])
def edit_user(user_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'address', 'email', 'position', 'speciality']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    user.surname = request.json['surname'],
    user.name = request.json['name'],
    user.age = request.json['age'],
    user.address = request.json['address'],
    user.email = request.json['email'],
    user.position = request.json['position'],
    user.speciality = request.json['speciality']
    db_sess.commit()
    return jsonify({'success': 'OK'})

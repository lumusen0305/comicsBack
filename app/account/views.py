import uuid

from sqlalchemy import text
from . import account
from databases import Account
from flask import request, jsonify

# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token,
#     jwt_refresh_token_required, create_refresh_token,
#     get_jwt_identity
# )
from manage import flask_uuid,JWTManager, jwt_required, create_access_token, create_refresh_token,get_jwt_identity
# from manage import flask_jwt_extended

#register
@account.route('/register' , methods=['POST'])
def register():
    user_id=uuid.uuid4()
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    user=Account(id=str(user_id),username=username,password=password,email=email)
    result=Account.judge_account_register(user)
    if result:
        Account.add(user)
        if user != None:
            return_dict = {
                "data": True,
                "code": 200,
                "msg": "註冊成功"
            }
        else:
            return_dict = {
                "data": False,
                "code": 423,
                "msg": "註冊失敗"
            }
    else:
        return_dict = {
           "data": False,
           "code": 200,
           "msg": "此帳號不可使用"
            }

    return jsonify(return_dict),200

#login
@account.route('/login' , methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = Account(id="id",username=username, password=password, email="email")

    result = Account.check(user)
    if result:
        print(True)
        ret = {
            'access_token': create_access_token(identity=username),
            'refresh_token': create_refresh_token(identity=username)
    }
    else:
        print(False)
        return jsonify({"msg": "Bad username or password"}), 401
        ret = {
            'msg':"Bad username or password"
    }
    # Use create_access_token() and create_refresh_token() to create our
    # access and refresh tokens
    return jsonify(ret), 200

@account.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200

@account.route('/protected', methods=['GET'])
@ jwt_required()
def protected():
    username = get_jwt_identity()
    return jsonify(logged_in_as=username), 200
#update
@account.route('/update' , methods=['PUT'])
def update():
    user_id =  request.form.get('user_id')
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    username = str(username)
    password = str(password)
    email = str(email)
    users = Account(username=username, password=password, email=email)
    result=Account.update(users,user_id)
    print(result)
    return_dict = {
       "data": True,
       "code": 200,
       "msg": "修改成功"
        }
    return jsonify(return_dict),200

@account.route('/test' , methods=['GET'])
def test():
    username = request.json.get('username')
    username = str(username)
    users = Account(id="id",username=username, password="password", email="email")
    result=Account.judge_account_register(users)
    if result:
        return_dict = {
           "data": True,
           "code": 200,
           "msg": "此帳號可使用"
            }
    else:
        return_dict = {
           "data": False,
           "code": 200,
           "msg": "此帳號不可使用"
            }
    return return_dict


#search
@account.route('/search' , methods=['GET'])
def search():
    username = request.json.get('username')
    username = str(username)
    users = Account(id="id",username=username, password="password", email="email")
    result=Account.search(users)
    user_dict = {
        "id": result.id,
        "username": result.username,
        "password": result.password,
        "email": result.email
    }
    return_dict = {
       "data": True,
       "code": 0,
       "msg": user_dict
        }
    return jsonify(return_dict)
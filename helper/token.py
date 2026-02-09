import jwt 
from datetime import datetime , timezone ,timedelta
from dotenv import load_dotenv
import os
from flask import request  , jsonify
from models import UserModel
from functools import wraps
load_dotenv()

def create_access_token(user_id):
    token = jwt.encode(
                    {'user_id': user_id,
                        'exp': datetime.now(timezone.utc) + timedelta(hours=1)
                    },
                    os.getenv("SECRET_KEY"), algorithm="HS256"
                    )
    return token

def token_required(f):
    @wraps(f)
    def check_jwt_token():
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(
                token,
                os.getenv("SECRET_KEY"),
                algorithms=["HS256"]
            )
            print(data, "00000000000000")

            current_user = UserModel.query.filter_by(
                id=data['user_id']
            ).first()

            if not current_user:
                return jsonify({'message': 'User not found'}), 401

        except Exception as e:
            return jsonify({
                'message': 'Token is invalid!',
                'error': str(e)
            }), 401

        return f(current_user)

    return check_jwt_token
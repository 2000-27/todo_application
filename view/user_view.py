from flask import Blueprint , jsonify , request, make_response
from models import UserModel
from schema import UserSchema
from marshmallow import ValidationError
import jwt
from config import db
from helper import create_access_token , token_required


user_bp = Blueprint("user_blueprint",__name__,url_prefix="/api")



@user_bp.route("/signup",methods=["POST"])
def signup():
    try:
        user_schema = UserSchema()
        data = user_schema.load(request.get_json())
        email = data.get("email")
        existing_user = UserModel.query.filter_by(email=email).first()
        if existing_user:
            return jsonify(
                {
                    "message":"This email is already register please login",
                    "status":400
                }
            ) ,400
        
        new_user = UserModel(**data)
        new_user.set_password(data.get("password"))
        db.session.add(new_user)
        db.session.commit()

    
        return jsonify(
            {
                "message":"user has been created successfully",
                "status":200
            }
        ) ,200
    except ValidationError as err:
            # Return validation errors as a JSON response
            print("***********************************",err)
            return jsonify({
                "message":err.messages ,
                "status": 400
            }) , 400
    except Exception as e:
        return jsonify(
            {
                "message":str(e),
                "status":400
            }
        ) ,400



@user_bp.route("/login",methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get("email")
        existing_user = UserModel.query.filter_by(email=email).first()
        if not existing_user:
            return jsonify(
                {
                    "message":"Please register your self",
                    "status":400
                }
            ) ,400
        
        if not existing_user.check_password(data.get("password")):
            return jsonify(
                {
                    "message":"Invalid creads",
                    "status":400
                }
            ) ,400
        
        token = create_access_token(existing_user.id)
        return jsonify({
            "access_token":token,
            "message":"login successfully",
            "status": 200
        }) , 200
    

    except Exception as e:
        return jsonify(
            {
                "message":str(e),
                "status":400
            }
        ) ,400
    



@user_bp.route("/get_details",methods=['GET'])
@token_required
def get_user_details(current_user):
    try:
        return jsonify({
            "user_id":current_user.id,
            "email":current_user.email,
            "message":"User found successfully",
            "status": 200
        }) , 200
    except Exception as e:
        return jsonify(
            {
                "message":str(e),
                "status":400
            }
        ) ,400
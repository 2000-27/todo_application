from flask import Blueprint , jsonify ,request
from models import TaskModel
from helper import token_required
from config import db
from schema import TaskSchema
from marshmallow import ValidationError

task_bp = Blueprint("task bp",__name__,url_prefix="/api")



@task_bp.route("/create_task",methods=["POST"])
@token_required
def create_task(current_user):
    try:
        task_schema = TaskSchema()
        data = task_schema.load(request.get_json())
        data["user_id"] = current_user.id
        task_info = TaskModel(**data)
        db.session.add(task_info)
        db.session.commit()
        return jsonify(
            {   
                "message":"task has been created successfully",
                "task_id":task_info.id,
                "status":200
            }
        ) ,200 
    except ValidationError as err:
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
        


@task_bp.route("/get_task",methods=["GET"])
@token_required
def get_single_task(current_user):
    try:
        task_schema =  TaskSchema(many=True)
        task_id = request.args.get("task_id")
        if task_id :
            all_task = TaskModel.query.filter_by(user_id=current_user.id,id=task_id).all()
        else:
            all_task = TaskModel.query.filter_by(user_id=current_user.id).all()
        
        all_task = task_schema.dump(all_task)
        return jsonify(
            {    "message":"Task found Successfully",
                "details":all_task,
                "status":200
            }
        ) ,200 
    except Exception as e:
        return jsonify(
            {
                "message":str(e),
                "status":400
            }
        ) ,400
    

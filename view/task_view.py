from flask import Blueprint , jsonify
from models import TaskModel
from helper import token_required

task_bp = Blueprint("task bp",__name__,url_prefix="/api")



@task_bp.route("/create_task",methods=["GET"])
@token_required
def create_task(current_user):
    print(current_user)
    print("we are createing a task")
    print("adding this line in from the browser")
    print("adding second line from the repo")
    return jsonify(
        {
            "message":"task has been created successfully",
            "status":200
        }
    ) ,200

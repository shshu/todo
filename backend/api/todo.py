from http import HTTPStatus

from app import app, bcrypt, db
from flask import abort, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from models.task import Task, create_task_by_user_id, get_tasks
from models.user import get_user
from sqlalchemy.exc import SQLAlchemyError


def show_user_todo_list(user_id):
    tasks = get_tasks(user_id=user_id)
    return jsonify(tasks=tasks), HTTPStatus.BAD_REQUEST

@app.route("/api/todo/<username>", methods=['GET', 'POST'])
# TODO need to jwt authenticate
def todo(username):
    # get user identiy from jwt TODO
    usr = get_user('admin')
    if not usr:
        return jsonify(error=f'Error: did not found user: {username}'), HTTPStatus.BAD_REQUEST
    
    if request.method == 'GET':
        return show_user_todo_list(usr.id)

    # POST 
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify(error='expected format {task: value}'), HTTPStatus.BAD_REQUEST
    
    task = create_task_by_user_id(data['task'], usr.id)
    return jsonify(task=f'created new task {task} for user {username}'), HTTPStatus.CREATED
 
@app.route("/api/todo/task/<int:id>", methods=['PATCH', 'DELETE'])
def update_task(id):
    pass

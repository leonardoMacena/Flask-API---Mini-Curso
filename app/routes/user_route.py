from app.controllers.user_controller import *
from flask import Blueprint, request, jsonify


bp_users = Blueprint('bp_users', __name__)

@bp_users.route('<user_id>', methods=['GET'])
def get_user (user_id):
  controller = UserController()
  controller.get(user_id)
  return jsonify(controller.content), controller.status

@bp_users.route('', methods=['POST'])
def create_user ():
  data = request.get_json()
  controller = UserController()
  controller.save(data)
  return jsonify(controller.content), controller.status

@bp_users.route('<user_id>', methods=['PUT'])
def update_user (user_id):
  data = request.get_json()
  controller = UserController()
  controller.update(user_id, data)
  return jsonify(controller.content), controller.status

@bp_users.route('<user_id>', methods = ['DELETE'])
def delete_user (user_id):
  controller = UserController()
  controller.remove(user_id)
  return jsonify(controller.content), controller.status

from app.controllers.user_controller import *
from flask import Blueprint, request, jsonify
from app.utils.auth import authentication


bp_users = Blueprint('bp_users', __name__)

@bp_users.route('', methods=['GET'])
@authentication
def get_user (user_id):
  print(request.headers['Authorization'])
  controller = UserController()
  controller.get(user_id)
  return jsonify(controller.content), controller.status

@bp_users.route('', methods=['POST'])
def create_user (user_id):
  print(test, 'deu certo')
  data = request.get_json()
  controller = UserController()
  controller.save(data)
  return jsonify(controller.content), controller.status

@bp_users.route('', methods=['PUT'])
@authentication
def update_user (user_id):
  data = request.get_json()
  controller = UserController()
  controller.update(user_id, data)
  return jsonify(controller.content), controller.status

@bp_users.route('', methods = ['DELETE'])
@authentication
def delete_user (user_id):
  controller = UserController()
  controller.remove(user_id)
  return jsonify(controller.content), controller.status

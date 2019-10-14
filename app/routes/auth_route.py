from app.controllers.auth_controller import AuthController
from flask import Blueprint, request, jsonify


bp_auth = Blueprint('bp_auth', __name__)

@bp_auth.route('', methods=['GET'])
def get_user (user_id):
  controller = AuthController()
  ip_address = request.remote_addr
  controller.get(user_id)
  return jsonify(controller.content), controller.status

@bp_auth.route('', methods=['POST'])
def create_user ():
  data = request.get_json()
  controller = AuthController()
  controller.save(data)
  return jsonify(controller.content), controller.status

@bp_auth.route('', methods=['PUT'])
def update_user (user_id):
  data = request.get_json()
  controller = AuthController()
  controller.update(user_id, data)
  return jsonify(controller.content), controller.status

@bp_auth.route('', methods = ['DELETE'])
def delete_user (user_id):
  controller = AuthController()
  controller.remove(user_id)
  return jsonify(controller.content), controller.status

from app.controllers.auth_controller import AuthController
from flask import Blueprint, request, jsonify


bp_auth = Blueprint('bp_auth', __name__)

@bp_auth.route('/token/refresh', methods=['GET'])
def get_user (user_id):
  controller = AuthController()
  ip_address = request.remote_addr
  controller.get(user_id)
  return jsonify(controller.content), controller.status

@bp_auth.route('/login', methods=['POST'])
def create_user ():
  data = request.get_json()
  ip_address = request.remote_addr
  controller = AuthController()
  controller.login(data, ip_address)
  return jsonify(controller.content), controller.status

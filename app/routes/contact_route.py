from app.controllers.contact_controller import ContactController
from flask import Blueprint, request, jsonify


bp_contact = Blueprint('bp_contact', __name__)

@bp_contact.route('/<user_id>', methods=['GET'])
def get_user (user_id):
  controller = ContactController()
  ip_address = request.remote_addr
  controller.get(user_id)
  return jsonify(controller.content), controller.status

@bp_contact.route('', methods=['POST'])
def create_user ():
  data = request.get_json()
  controller = UserController()
  controller.save(data)
  return jsonify(controller.content), controller.status

@bp_contact.route('/<user_id>', methods=['PUT'])
def update_user (user_id):
  data = request.get_json()
  controller = UserController()
  controller.update(user_id, data)
  return jsonify(controller.content), controller.status

@bp_contact.route('/<user_id>', methods = ['DELETE'])
def delete_user (user_id):
  controller = UserController()
  controller.remove(user_id)
  return jsonify(controller.content), controller.status

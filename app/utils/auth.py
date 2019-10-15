import jwt
import time
from app.config import get_jwt_lifetime_value, get_jwt_key
from flask import request, jsonify
from app.utils.common import AUTH, STATUS_CODE
from functools import wraps

def get_exp_time():
  return int(time.time()) + get_jwt_lifetime_value()

def create_token(user_id):
  payload = {
    'user_id': user_id,
    'exp': get_exp_time()
  }

  token = jwt.encode(payload, get_jwt_key(), algorithm='HS256')
  return token.decode('utf-8')


def decode(token):
    return jwt.decode(token, get_jwt_key(), verify=True, algorithm='HS256')

def authentication (f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if not request.headers.get('Authorization'):
      return jsonify({'error': AUTH['TOKEN']['NOT_FOUND']}), STATUS_CODE['BAD_REQUEST']
    try:
      token = get_token(request.headers.get('Authorization'))
      decode_token = decode(token)
      return f(decode_token.get('user_id'), *args, **kwargs)
    except jwt.ExpiredSignatureError:
      return jsonify({ 'error': AUTH['TOKEN']['TIMEOUT'] }), STATUS_CODE['UNAUTHORIZED']
    except jwt.InvalidTokenError:
      return jsonify({'error': AUTH['TOKEN']['INVALID_TOKEN']}), STATUS_CODE['UNAUTHORIZED']
  return decorated

def get_token(token):
  return token.split(' ')[1]

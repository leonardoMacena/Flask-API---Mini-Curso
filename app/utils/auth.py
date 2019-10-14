import jwt
from time import time
from app.config import *


def create_token(payload):
  token = jwt.encode(payload, get_jwt_key, algorithm='HS256')
  str_token = token.decode('utf-8')
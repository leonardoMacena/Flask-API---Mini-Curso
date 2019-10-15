from app.utils.encrypt import validete
from app.utils.auth import create_token
from app.utils.common import AUTH, STATUS_CODE, USER
from app.services.user_service import UserService

class AuthController:

  def __init__(self):
    self.status = None
    self.content = None
    self.__errors = []
    self.__user_service = UserService()

  def login(self, data):
    try:
      __email = data.get('email')
      __password = data.get('password')
      __user = self.__user_service.get_by_email(__email)
      if validete(__password, __user.password):
        token = create_token(__user.id)
        self.content = { 'token': token }
        self.status = STATUS_CODE['OK']

      else:
        self.content = { 'error': AUTH['LOGIN'] }
        self.status = STATUS_CODE['BAD_REQUEST']

    except Exception as error:
      print(e)
      self.content = { 'error': AUTH['LOGIN'] }
      self.status = STATUS_CODE['BAD_REQUEST']

  def refresh_token(self, user_id):
    pass

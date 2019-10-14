from app.utils.common import STATUS_CODE, USER

from app.services.user_service import *

class UserController():
  def __init__(self):
    self.status = None
    self.content = None
    self.__errors = []
    self.__service = UserService()

  def get(self, user_id):
    __user = self.__service.get(user_id)
    if not __user:
      self.content = { 'error': USER['NOT_FOUND'] }
      self.status = STATUS_CODE['NOT_FOUND']
    else:
      self.content =  { 'data': __user.toDICT() }
      self.status = STATUS_CODE['OK']

  def save(self, data):
    self.__verify_filds(data)
    __user = self.__service.get_by_email(data.get('email'))

    if __user:
      self.__errors.append(USER['EMAIL']['REGISTERED'])

    if len(self.__errors) > 0:
      self.content = { 'errors': self.__errors }
      self.status = STATUS_CODE['BAD_REQUEST']
    else:
      self.__service.save(data)
      self.content = { 'data': 'created user' }
      self.status = STATUS_CODE['CREATED']

  def update(self, user_id, data):
    self.__verify_filds(data)
    __user = self.__service.get(user_id)

    if not __user:
      __errors.append(USER['NOT_FOUND'])

    if len(self.__errors) > 0:
      self.content = { 'errors': self.__errors }
      self.status = STATUS_CODE['BAD_REQUEST']
    else:
      __updated_user = self.__service.update(__user, data)
      self.content = __updated_user.toDICT()
      self.status = STATUS_CODE['OK']


  def remove(self, user_id):
    __user = self.__service.get(user_id)
    if not __user:
      self.__errors.append(USER['NOT_FOUND'])
      self.content = { 'errors': self.__errors }
      self.status = STATUS_CODE['NOT_FOUND']
    else:
      self.__service.remove(__user)
      self.content = {'data': USER['SUCCESS']}
      self.status = STATUS_CODE['OK']

  def __verify_filds(self, data):
    if not data['email']:
      self.__errors.append(USER['EMAIL']['NOT_FOUND'])

    if not data['name']:
      self.__errors.append(USER['NAME']['NOT_FOUND'])

    if not data['password']:
      self.__errors.append(USER['PASSWORD']['NOT_FOUND'])

    if not data['phone']:
      self.__errors.append(USER['PHONE']['NOT_FOUND'])

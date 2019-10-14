from app import db
from app.models.user import User
from app.services.service import Service
from app.utils.encrypt import *

class UserService(Service):

  def save(self, data):
    __pwdHash = encrypt(data.get('password'))
    __user = User(
      password = __pwdHash,
      name = data.get('name'),
      email = data.get('email'),
      phone = data.get('phone')
    )
    db.session.add(__user)
    db.session.commit()
    return __user.id

  def get(self, user_id):
    return User.query.filter_by(id=user_id).first()

  def get_by_email(self, email):
    return User.query.filter_by(email = email).first()

  def update(self, user, data):
    user.name = super().get_key_from_dict('name', data, user.name)
    user.email = super().get_key_from_dict('email', data, user.email)
    user.phone = super().get_key_from_dict('phone', data, user.email)
    db.session.commit()
    return self.get(user.id)

  def remove(self, user):
    db.session.delete(user)
    db.session.commit()
    return True

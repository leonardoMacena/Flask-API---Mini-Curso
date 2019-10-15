from app import db
from app.models.login import Login


class LoginService:

  def save(self, user_id, ip):
    __login = Login(
      user_id = user_id,
      ip_address = ip
    )
    db.session.add(__login)
    db.session.commit()

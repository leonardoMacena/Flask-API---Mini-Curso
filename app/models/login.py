from app import db
from datetime import datetime

class Login(db.Model):
  user_id = db.Column(db.INTEGER, primary_key=True)
  timestamp = db.Column(db.INTEGER, unique=False, nullable=False)
  ip_address = db.Column(db.TEXT, nullable=False)

  def __repr__(self):
      return '<Login id:%r>' % self.user_id

  def toDICT(self):
      return {
          'user_id': self.user_id,
          'timestamp': self.timestamp,
          'ip_address': self.ip_address
          }

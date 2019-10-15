from app import db
from datetime import datetime

class Login(db.Model):
  id = db.Column(db.INTEGER, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  timestamp = db.Column(db.DateTime, default=datetime.now())
  ip_address = db.Column(db.TEXT, nullable=False)

  def __repr__(self):
      return '<Login id:%r>' % self.user_id

  def toDICT(self):
      return {
          'user_id': self.user_id,
          'timestamp': self.timestamp.timestamp(),
          'ip_address': self.ip_address
        }

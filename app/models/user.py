from app import db
from datetime import datetime

class User (db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  password = db.Column(db.String(200), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  name = db.Column(db.String(120), nullable=False)
  phone = db.Column(db.String(50), nullable=False)
  created = db.Column(db.DateTime, default=datetime.now())

  def __repr__(self):
    return '<User %r>' % self.name

  def toDICT (self):
    return {
      'id': self.id,
      'name' : self.name,
      'created': self.created.timestamp(),
      'email': self.email,
      'phone': self.phone
    }

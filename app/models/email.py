from app import db
from datetime import datetime

class Email (db.Model):
  __tablename__ = 'email'

  id = db.Column(db.Integer, primary_key=True)
  contato_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
  address = db.Column(db.String(120), unique=True, nullable=False)

  def __repr__(self):
    return '<Email %r>' % self.address

  def toDICT (self):
    return {
      'id': self.id,
      'contato_id': self.contato_id,
      'address': self.address
    }

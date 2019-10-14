from app import db
from datetime import datetime

class Phone (db.Model):
  __tablename__ = 'phone'

  id = db.Column(db.Integer, primary_key=True)
  contato_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
  number = db.Column(db.String(50), unique=True, nullable=False)

  def __repr__(self):
    return '<Phone %r>' % self.number

  def toDICT (self):
    return {
      'id': self.id,
      'contato_id': self.contato_id,
      'number': self.number
    }

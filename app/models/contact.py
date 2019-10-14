from app import db
from datetime import datetime

class Contact (db.Model):
  __tablename__ = 'contact'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), unique=True, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  created = db.Column(db.DateTime, default=datetime.now)
  updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

  def __repr__(self):
        return '<Contato %r>' % self.name

  def toDICT(self):
    return {
      'id': self.id,
      'name': self.name,
      'created': self.created,
      'updated': self.updated
    }

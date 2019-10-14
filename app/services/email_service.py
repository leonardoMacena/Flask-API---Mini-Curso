from app import db
from app.models.email import Email
from app.services.service import Service

class EmailService(Service):
  def save(self, data):
    __email = Email(
      contato_id = data.get('contato_id'),
      address = data.get('address')
    )
    db.session.add(__email)
    db.session.commit()

  def get(self, contato_id):
    return Email.query.filter_by(contato_id = contato_id).all()

  def update(self, email, data):
    email.address = super().get_key_from_dict('adrress', data, email.address)
    db.session.commit()
    return self.get(email.contato_id)

  def remove(self, email):
    db.session.delete(email)
    db.session.commit()
    return True

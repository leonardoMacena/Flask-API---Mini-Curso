from app import db
from app.models.phone import Phone
from app.services.service import Service

class PhoneService(Service):
  def save(self, data):
    __phone = Phone(
      contato_id = data.get('contato_id'),
      nnumer = data.get('number')
    )
    db.session.add(__phone)
    db.session.commit()

  def get(self, contato_id):
    return Phone.query.filter_by(contato_id = contato_id).all()

  def update(self, phone, data):
    phone.numer = super().get_key_from_dict('number', data, phone.numer)
    db.session.commit()
    return self.get(phone.contato_id)

  def remove(self, phone):
    db.session.delete(phone)
    db.session.commit()
    return True

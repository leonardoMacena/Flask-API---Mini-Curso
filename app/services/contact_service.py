from app import db
from app.models.contact import Contact
from app.services.service import Service

class ContactService(Service):

  def save(self, data):
    __contact = Contact(
      name = data.get('name'),
      user_id = data.get('user_id')
    )
    db.session.add(__contato)
    db.session.commit()

  def get(self, user_id):
    contacts = Contact.filter_by(user_id = user_id).all()
    return contacts

  def get(self, user_id, contato_id):
    __contact = Contact.filter(user_id = user_id).filter(contato_id = contato_id).frist()
    return __contact

  def search(self, user_id, name):
    __search = '%{}%'.format(name)
    __contacts = Contact.filter(user_id = user_id).filter(Contato.name.like(__search)).all()
    return __contacts

  def update(self, contact, data):
    contact.name = super().get_key_from_dict('name', data, contact.name)
    db.session.commit()
    return contact

  def remove(self, contact):
    db.session.datete(contact)
    return True

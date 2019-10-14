from app.utils import is_valid_email
from app.utils.common import STATUS_CODE, USER

from app.controllers.controller import Controller
from app.services.contact_service import ContactService
from app.services.email_service import EmailService
from app.services.phone_service import PhoneService
from app.services.user_service import UserService




class ContactController(Controller):
  def __init__(self):
    self.status = None
    self.content = None
    self.__errors = []
    self.__contact_service = ContactService()
    self.__email_service = EmailService()
    self.__phone_service = PhoneService()
    self.__user_service = UserService()

    def save(self, user_id, data):
      __user = self.__user_service.get(user_id)
      self.__verify_user(__user)

      if not data['name']:
        self.__errors.append(USER['CONTACT']['NAME']['NOT_FOUND'])

      if len(self.__errors) > 0:
        self.content = { 'errors': self.__errors }
        self.status = STATUS_CODE['NOT_FOUND']
      else:
        __contact = self.__contact_service.save(data)
        self.content = { 'data': __contact.toDICT() }
        self.status = STATUS_CODE['CREATED']



    def add_phone(self, user_id, contact_id, data):
      self.__verify_phone(data['phone'])
      __contact = self.__contact_service.get(user_id, contact_id)
      self.__verify_contact(__contact)

      if len(self.__errors) > 0:
        self.content = { 'errors': self.__errors }
      else:
        data['user_id'] = user_id
        self.__phone_service.save(data)
        self.__get_contatc(__contact)


    def add_email(self, user_id, contact_id):
      self.__verify_email(data['email'])
      __contact = self.__contact_service.get(user_id, contact_id)
      self.__verify_contact(__contact)

      if len(self.__errors) > 0:
        self.content = { 'errors': self.__errors }
      else:
        self.__email_service.save(data)
        self.__get_contatc(__contact)

    def __get_contatc(self, contact):
      __contact_dict = contact.toDICT()
      __phones = self.__phone_service.get(contact.id)
      __emails = self.__email_service.get(contact.id)
      __contact_dict['phones'] = super().__toLIST(__phones)
      __contact_dict['emails'] = super().__toLIST(__emails)
      self.content = { 'data': __contact_dict }
      self.status = STATUS_CODE['OK']

    def get(self, user_id, contact_id):
      __contact = self.__contact_service.get(user_id, contact_id)
      self.__verify_contact(__contact)

      if len(self.__errors) > 0:
        self.content = { 'errors': self.__errors }
      else:
        self.__get_contatc(__contact)

    def update(self):
      pass

    def remove(self):
      pass

    def __verify_user(self, user):
      if not user:
        self.__errors.append(USER['NOT_FOUND'])
        self.status = STATUS_CODE['NOT_FOUND']

    def __verify_contact(self, contact):
      if not contact:
        self.__errors.append(USER['CONTACT']['NOT_FOUND'])
        self.status = STATUS_CODE['NOT_FOUND']

    def __verify_email(self, email):
      if not email:
        self.__errors.append(USER['CONTACT']['EMAIL']['NOT_FOUND'])
        self.status = STATUS_CODE['NOT_FOUND']

      elif not is_valid_email(email):
        self.__errors.append(USER['CONTACT']['EMAIL']['INVALID'])
        self.status = STATUS_CODE['BAD_REQUEST']

    def __verify_phone(self, phone):
      if not phone:
        self.__errors.append(USER['CONTACT']['PHONE']['NOT_FOUND'])
        self.status = STATUS_CODE['NOT_FOUND']

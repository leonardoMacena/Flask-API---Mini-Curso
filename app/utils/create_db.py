def init_db():
  print('init db')
  try:
    from app.models.contact import Contact
    from app.models.user import User
    from app.models.phone import Phone
    from app.models.email import Email
    from app.models.login import Login
    from app import db
    db.create_all()
  except Exception as error:
    print(error)

SERVICES = {
  'database_uri': 'sqlite:///test.db',
  'jwt_key': 'bolso_mago',
  'jwt_lifetime': 3600*6
}

def get_property_value(key):
  return SERVICES[key]

def get_database_uri_value():
  return get_property_value('database_uri')

def get_jwt_key():
  return get_property_value('jwt_key')

def get_jwt_lifetime_value():
  return get_property_value('jwt_lifetime')

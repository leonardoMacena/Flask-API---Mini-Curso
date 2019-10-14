STATUS_CODE = {
  'OK': 200,
  'CREATED': 201,
  'NO_CONTENT': 204,
  'BAD_REQUEST': 400,
  'UNAUTHORIZED': 401,
  'NOT_FOUND': 404,
  'INTERNAL_SERVER_ERROR': 500
}

USER = {
  'NOT_FOUND':'user not found',
  'EMAIL':{
    'NOT_FOUND': 'email not found',
    'INVALID': 'invalid email',
    'REGISTERED': 'email already registered'
  },
  'PASSWORD': {
    'NOT_FOUND': 'password not found',
    'SHORT': 'password too short'
  },
  'NAME': {
    'LONG': 'name too long',
    'NOT_FOUND': 'name not found'
  },
  'PHONE': {
    'NOT_FOUND': 'phone not found'
  },
  'CONTACT': {
    'NOT_FOUND': 'contact not found',
    'NAME': {
      'NOT_FOUND': 'contact name not found'
    },
    'EMAIL': {
      'NOT_FOUND': 'contact email not found'
    },
    'PHONE': {
      'NOT_FOUND': 'contact phone not found'
    }
  },
  'INTERNAL_SAVE_ERROR': 'error to save user',
  'SUCCESS': 'was a success'
}

AUTH = {
  'LOGIN': {
    'NO_REGISTER':'email not registered',
    'NOT_FOUND':'email not found',
    'WRONG_PASSWORD':'wrong password'
  },
  'NOT_AUTH':'not authorized',
  'INVALID_TOKEN':'invalid token',
}

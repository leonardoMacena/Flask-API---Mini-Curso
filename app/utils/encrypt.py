import bcrypt

def encrypt (pwd):
  salt = bcrypt.gensalt(rounds=10)
  hashed = bcrypt.hashpw(str.encode(pwd), salt)
  return hashed.decode()

def validete(pwd, encryptPwd):
    result = bcrypt.checkpw(str.encode(pwd), str.encode(encryptPwd))
    return result

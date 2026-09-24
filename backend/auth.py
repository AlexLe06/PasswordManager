from . import schemas
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def find_user():
    pass

def verify_password(password, stored_hash):
    return bcrypt.checkpw(password.encode, stored_hash.encode())



from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class HashPassword:
    def __init__(self):
        pass
    def hash_password(self, password):
        return pwd_context.hash(password)
    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
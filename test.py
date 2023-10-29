a = 10
b = bin(a)
x = bytes(b)
from cryptography.fernet import Fernet
c = Fernet.generate_key()
d = Fernet(c).encrypt(x)
import bcrypt
import hashlib



first = "hello"
second = "world"

salt = bcrypt.gensalt()

bcrypt.hashpw(b"hello", salt)

bcrypt.hashpw(b"world", salt)


hashed_value = bcryp.hashpw(b"world", salt)

int(hashed_value)
import hashlib

password = 'hello world'

hash = hashlib.md5(password.encode()).hexdigest()
print(hash)
print(password.encode())


hello world

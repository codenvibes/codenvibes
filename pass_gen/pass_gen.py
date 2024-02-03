#!/usr/bin/python
# AUTH: codenvibes
"""
"""
import random
import string


def generate_password(length=None):
    if length is None:
        length = int(input("Enter password length: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        return(password)

password = generate_password()
print(password)

#!/usr/bin/python3
# AUTH: codenvibes
"""
This script generates a random password of the specified length.
"""
import random
import string


def generate_password(length=None):
    """
    Generates a random password of the specified length.

    Args:
    - length (int): The length of the password to generate.
      If not provided, the user will be prompted to enter a length.

    Returns:
    - str: The generated password.
    """
    if length is None:
        length = int(input("Enter `password length: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        return (password)


password = generate_password()
print(password)

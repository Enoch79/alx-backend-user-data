#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password

password = "84279Young"
print(hash_password(password))
print(hash_password(password))

"""
Generate a random password.
Code from http://code.activestate.com/recipes/59873-random-password-generation/
"""

from random import choice
import string

def GenPasswd():
    chars = string.letters + string.digits
    for i in range(8):
        newpasswd = newpasswd + choice(chars)
    return newpasswd

def GenPasswd2(length=8, chars=string.letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])


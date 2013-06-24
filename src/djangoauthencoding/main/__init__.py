from hashlib import sha1
from AccessControl.AuthEncoding import registerScheme
import random


def sha1hash(salt, string):
    """Provide a SHA1 hexdigest of string, salted with salt."""
    return sha1(salt + string).hexdigest()


class DjangoSHAScheme:

    def encrypt(self, pw):
        salt = sha1hash(str(random.random()), str(random.random()))[:5]
        return sha1hash(salt, pw)

    def validate(self, reference, attempt):
        method, salt, hashed = reference.split('$')
        return sha1hash(salt, attempt) == hashed


def initialize(registrar):
    registerScheme('sha1', DjangoSHAScheme())

# Embedded file name: PyLock.py
import sys, os
from itertools import cycle, izip
import base64

class XorLock:

    def __init__(self):
        pass

    def encode(self, script, key):
        encoded = ''.join((chr(ord(c) ^ ord(k)) for c, k in izip(script, cycle(key))))
        return base64.b64encode(encoded)

    def decode(self, script, key):
        script = base64.b64decode(script)
        return ''.join((chr(ord(c) ^ ord(k)) for c, k in izip(script, cycle(key))))


class PyLock:

    def __init__(self, script):
        self.script = script
        self.keys = []

    def run(self):
        exec self.script

    def save(self):
        return self.script

    def lock(self, Locker, key):
        locker = Locker()
        self.script = locker.encode(self.script, key)
        self.keys.append([Locker.__name__, key])

    def unlock(self, Locker, key):
        locker = Locker()
        self.script = locker.decode(self.script, key)
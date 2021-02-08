'''Modul'''
from person import Person
class Sender(Person):
    '''Sender class'''
    def operate_cipher(self, cipher, text):
        return cipher.encode(text, self.get_key())

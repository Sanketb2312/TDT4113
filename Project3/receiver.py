'''Modul'''
from person import Person
class Receiver(Person):
    '''Receiver class'''
    def operate_cipher(self, cipher, text):
        return cipher.decode(text, self.get_key())

'''Modul'''
from person import Person
from caesar import Caesar
class Receiver(Person):
    '''Receiver class'''
    def operate_cipher(self, cipher, text):
        return cipher.decode(text, self.get_key())

#r = Receiver(2)
#c = Caesar()
#print(r.operate_cipher(c, c.encode("hello", 2)))
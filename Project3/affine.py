'''Modul'''
from cipher import Cipher
from multiplicative import Multiplicative
from caesar import Caesar
class Affine(Cipher):
    '''Affine class'''

    def encode(self, text, key):
        multi = Multiplicative().encode(text,key[0])
        return Caesar().encode(multi,key[1])

    def decode(self, text, key):
        caesar = Caesar().decode(text,key[1])
        return Multiplicative().decode(caesar, key[0])

    def generate_keys(self):
        return [Multiplicative().generate_keys(), Caesar().generate_keys()]

    def possible_keys(self):
        return Multiplicative().possible_keys()

#a = Affine()
#print(Cipher.verify(a, "Tester 123", a.generate_keys()))

'''Modul'''
import random
from receiver import Receiver
from caesar import Caesar
from multiplicative import Multiplicative
from affine import Affine
from unbreakable import Unbreakable
from rsa import RSA
from cipher import Cipher

class Hacker(Receiver):
    '''Hacker class'''
    def __init__(self, cipher):
        self.cipher = cipher


    def english_words(self):
        '''List of the txt file'''
        file = open('english_words.txt')
        return file.read().splitlines()

    def brute_force(self, cipher, crypt_key):
        '''Brute force method'''
        words = self.english_words()
        for key in cipher.possible_keys():
            if isinstance(cipher, Affine):
                for key_two in cipher.possible_keys():
                    self.set_key([key, key_two])
                    if self.operate_cipher(cipher, crypt_key) in words:
                        return self.operate_cipher(cipher, crypt_key)
            else:
                self.set_key(key)
                if words.__contains__(self.operate_cipher(cipher, crypt_key)):
                    return self.operate_cipher(cipher,crypt_key)

        return "None of the possible keys could decrypt the encrypted word"

c = Caesar()
h =Hacker(c)
print(h.brute_force(c, c.encode("hello", c.generate_keys())))

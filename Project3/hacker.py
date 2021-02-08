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
        return open('english_words.txt').readlines()

    def brute_force(self, cipher, crypt_key):
        '''Brute force method'''
        for key in cipher.possible_keys():
            if isinstance(cipher, Affine):
                for key_two in cipher.possible_keys():
                    self.set_key([key, key_two])
                    if self.operate_cipher(cipher, crypt_key) in self.english_words():
                        return self.operate_cipher(cipher, crypt_key)
            else:
                self.set_key(key)
                if self.operate_cipher(cipher,crypt_key) in self.english_words():
                    return self.operate_cipher(cipher,crypt_key)

        return "None of the possible keys could decrypt the encrypted word"

c = Multiplicative()
h =Hacker(c)
h.brute_force(c, c.encode(h.english_words()
                          [random.randint(0, len(h.english_words()))], c.generate_keys()))

'''Modul'''
from cipher import Cipher
import crypto_utils
import random
class Multiplicative(Cipher):
    '''Multiplicative class'''
    def encode(self, text, key):
        encoded_text = ""
        for x in range (len(text)):
            if self.alphabet_min > ord(text[x]) > self.alphabet_max:
                continue

            coded_value = ((ord(text[x]))*key-self.alphabet_min) %\
                          self.alphabet_length()+self.alphabet_min
            encoded_text+=chr(coded_value)
        return encoded_text


    def decode(self, text, key):
        x = crypto_utils.modular_inverse(key, self.alphabet_length())
        return self.encode(text, x)

# only keys with gcd(x,m)=1 have an inverse.
# Since we use module alphabet.length(), we check if gcd(key, alphabet.length())=1
    def generate_keys(self):
        return self.possible_keys()[random.randint(0, len(self.possible_keys())-1)]

    def possible_keys(self):
        valid_keys=[]
        for key in range(0, self.alphabet_length()):
            if crypto_utils.extended_gcd(key, self.alphabet_length())[0]==1:
                valid_keys.append(key)
        return valid_keys


m = Multiplicative()
print(Cipher.verify(m,"Tester 123",m.generate_keys()))

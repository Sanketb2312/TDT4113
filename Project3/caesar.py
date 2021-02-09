'''Modul'''
import random
from cipher import Cipher
class Caesar(Cipher):
    '''Caeser class'''
    def encode(self, text, key):
        encoded_text = ""
        for val in range (0, len(text)):
            if self.alphabet_min> ord(text[val])> self.alphabet_max:
                continue
            coded_value = (ord(text[val])+key-self.alphabet_min) \
                          % self.alphabet_length()+self.alphabet_min
            encoded_text+=chr(coded_value)

        return encoded_text

    def decode(self, text, key):
        return self.encode(text, self.alphabet_length()-key)

    def generate_keys(self):
        return random.randint(0, self.alphabet_length())
    def possible_keys(self):
        possible_keys_list = []
        for val in range(self.alphabet_length()):
            possible_keys_list.append(val)
        return possible_keys_list

#c = Caesar()
#print(Cipher.verify(c, "Tester 123", c.generate_keys()))



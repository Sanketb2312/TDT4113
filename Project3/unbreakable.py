'''Modul'''
from cipher import Cipher
import random

class Unbreakable(Cipher):
    '''Unbreakable class'''
    def encode(self, text, key):
        word = self.creat_keyword(text,key)
        encoded_word = ""
        for val in range(len(text)):
            if(self.alphabet_min> ord(text[val])> self.alphabet_max) or \
                    (self.alphabet_min> ord(word[val])> self.alphabet_max):
                continue
            curr_value = (ord(text[val])+ord(word[val])-self.alphabet_min) \
                         % self.alphabet_length()+self.alphabet_min
            encoded_word+=chr(curr_value)
        return encoded_word


    def decode(self, text, key):
        key_word_list=[]
        for val in range(len(key)):
            key_word_list.append((self.alphabet_length()-ord(key[val])-self.alphabet_min)%
                                 self.alphabet_length()+self.alphabet_min)
        decode_key_word = ""
        for i in range(len(key_word_list)):
            decode_key_word+=chr(key_word_list[i])
        return self.encode(text,decode_key_word)

    def generate_keys(self):
        '''generating keys'''
        return self.possible_keys()[random.randint(0, len(self.possible_keys()))]

    def possible_keys(self):
        return open('english_words.txt').readlines()

    def creat_keyword(self, text, keyword):
        '''creating a word of same length as keyword'''
        word = ""
        counter = 0
        for count in range(len(text)):
            if counter >= len(keyword):
                counter = 0
            word += keyword[counter]
            counter += 1
        return word


#u = Unbreakable()
#print(Cipher.verify(u, "Tester 123", u.generate_keys()))

'''Modul'''
class Cipher:
    '''Modul'''
    def __init__(self):
        '''Constructer to set min and max value of the alphabet'''
        self.alphabet_min = 32
        self.alphabet_max = 126
    def encode(self, text, key):
        '''Method for encoding the text'''


    def decode(self, text, key):
        '''Method for decoding the encrypted message'''
        pass
    def generate_keys(self):
        '''generating a key for the specific cipher'''
        pass
    def verify(self, text, key):
        '''verify method to check if the doceded message of the encoded text is equal to the original text or not'''
        return text == self.decode(self.encode(text, key), key)

    def possible_keys(self):
        '''returns all possible keys for the specific cipher'''
        pass

    def alphabet_length(self):
        '''the length of the alphabet'''
        return self.alphabet_max-self.alphabet_min+1

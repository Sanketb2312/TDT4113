'''Modul'''
class Person:
    '''Person class'''

    def __init__(self, key):
        '''setting the key in constructor'''
        self.key = key

    def set_key(self,key):
        '''set key method used i hacker'''
        self.key = key
    def get_key(self):
        '''get key method'''
        return self.key
    def operate_cipher(self, cipher, text):
        '''method used to send en receive messages'''

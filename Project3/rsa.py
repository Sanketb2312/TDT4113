'''Modul'''
from cipher import Cipher
import crypto_utils
import random
class RSA(Cipher):
    '''RSA class'''

    def __init__(self):
        self.encryption_key = None
        self.decryption_key = None
        self.c_list = []


    def encode(self, text, key):
        blocks = crypto_utils.blocks_from_text(text, 2)
        self.c_list = []
        for block in blocks:
            self.c_list.append(pow(block,self.encryption_key[1], self.encryption_key[0]))
        return self.c_list

    def decode(self, text, key):
        decoded_blocks = []
        for val in self.c_list:
            decoded_blocks.append(pow(val, self.decryption_key[1], self.decryption_key[0]))
        return crypto_utils.text_from_blocks(decoded_blocks, 2)



    def generate_keys(self):
        while True:
            p_p = crypto_utils.generate_random_prime(8)
            q_q = crypto_utils.generate_random_prime(8)
            while q_q == p_p:
                q_q = crypto_utils.generate_random_prime(8)
            n_n=p_p*q_q
            phi = (p_p-1)*(q_q-1)
            e_e = random.randint(3, phi-1)
            d_d = crypto_utils.modular_inverse(e_e, phi)

            if d_d != None:
                break

        self.encryption_key=(n_n,e_e)
        self.decryption_key=(n_n,d_d)
        return (self.encryption_key, self.decryption_key)


    def convert_to_8bit_binary(self, integer):
        binary = bin(integer)
        binary=binary[2:]

        while len(binary) !=8:
            binary = '0'+binary
        return binary

#rsa = RSA()
#print(Cipher.verify(rsa, "Tester 123", rsa.generate_keys()))

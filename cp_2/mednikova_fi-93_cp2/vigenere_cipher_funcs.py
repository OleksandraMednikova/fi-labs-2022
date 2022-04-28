from typing import List 
from text_getter import alphabet

num_to_sym = {i: alphabet[i] for i in range(len(alphabet))}
sym_to_num = {alphabet[i]: i for i in range(len(alphabet))}
sym_amount = len(alphabet)

def vigenere_cipher(plaintext: str, key: str, sym_amount: int=sym_amount) -> str:
    ciphertext = ''
    r = len(key)
    for i in range(len(plaintext)):
        ciphertext += num_to_sym[(sym_to_num[plaintext[i]] + sym_to_num[key[i % r]]) % sym_amount]
    return ciphertext

def vigenere_decipher(ciphertext: str, key: str, sym_amount: int=sym_amount) -> str:
    plaintext = ''
    r = len(key)
    for i in range(len(ciphertext)):

        plaintext += num_to_sym[(sym_to_num[ciphertext[i]] - sym_to_num[key[i % r]]) % sym_amount]
    return plaintext

def vigenere_key_definer(plaintext: str, ciphertext: str, key_len: int, sym_amount: int=sym_amount) -> str:
    key = ''
    for i in range(key_len):
        
        key += num_to_sym[(sym_to_num[ciphertext[i]] - sym_to_num[plaintext[i]]) % sym_amount]
    return key
from typing import List 
from text_getter import alphabet

num_to_sym = {i: alphabet[i] for i in range(len(alphabet))}
sym_to_num = {alphabet[i]: i for i in range(len(alphabet))}
sym_amount = len(alphabet)

def vigenere_cipher(plaintext: str, key: List[str]) -> str:
    ciphertext = ''
    r = len(key)
    for i in range(len(plaintext)):
        ciphertext += num_to_sym[(sym_to_num[plaintext[i]] + sym_to_num[key[i % r]]) % sym_amount]
    
    return ciphertext


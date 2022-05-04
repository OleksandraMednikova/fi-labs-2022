from typing import List, Dict, Tuple
from text_getter.text_getter import alphabet
from math_operations.operations import inversed_element, extended_euclid

def sym_to_num(alphabet: List[str]) -> Dict[str, int]:
    return {alphabet[i]: i  for i in range(len(alphabet))}

def num_to_sym(alphabet: List[str]) -> Dict[int, str]:
    return {i: alphabet[i] for i in range(len(alphabet))}

def bigram_num(bigram: str, alphabet: List[str]=alphabet) -> int:
    sym_num = sym_to_num(alphabet)
    bigram_num = sym_num[bigram[0]] * len(alphabet) + sym_num[bigram[1]]
    return bigram_num

def bigrams_to_nums(alphabet: List[str]=alphabet) -> Dict[str, int] :
    bigrams_to_num = {}
    sym_amount = len(alphabet)
    for i in range(sym_amount):
        for j in range(sym_amount):
            bigram = alphabet[i] + alphabet[j]
            bigrams_to_num[bigram] = bigram_num(bigram)
    return bigrams_to_num

def nums_to_bigrams() -> Dict[int, str]:
    return {num: bigram for bigram, num in bigrams_to_nums().items()}

bigram_to_num = bigrams_to_nums()
num_to_bigram = nums_to_bigrams()

def text_to_bigrams(text: str) -> List[str]:
    letters_list = list(text)
    text_bigrams = [letters_list[i] + letters_list[i+1] for i in range(0, len(letters_list)-1, 2)]
    return text_bigrams

Key = Tuple[int, int]
def affine_cipher(plaintext: str, key: Key, alphabet: List[str]=alphabet) -> str:
    ciphertext = ''
    a, b = key
    module = len(alphabet) ** 2
    if 0 < a < module and 0 <= b < module and extended_euclid(a, module)[0] == 1: 
        plaintext_bigrams = text_to_bigrams(plaintext)
        for bigram in plaintext_bigrams:
            ciphertext += num_to_bigram[(a * bigram_to_num[bigram] + b) % module]
    return ciphertext

def affine_decipher(ciphertext: str, key: Key, alphabet: List[str]=alphabet) -> str:
    plaintext = ''
    a, b = key
    module = len(alphabet) ** 2
    inv_el = inversed_element(a, module)
    if 0 < a < module and 0 <= b < module and inv_el:
        ciphertext_bigrams = text_to_bigrams(ciphertext)
        for bigram in ciphertext_bigrams:
            plaintext += num_to_bigram[(inv_el * (bigram_to_num[bigram] - b)) % module]
    return plaintext
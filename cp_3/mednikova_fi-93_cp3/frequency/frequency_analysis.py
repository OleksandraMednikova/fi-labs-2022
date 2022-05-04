from typing import Union, List, Dict, Tuple, Set
from text_getter.text_getter import alphabet
from math_operations.operations import solve_congruence
from cipher.affine_cipher import bigram_to_num, affine_decipher

#Підрахунок кількості потрібних частинок у тексті
def symbol_frequency(text: Union[str, List[str]], sort: bool=False) -> Union[Dict[str, int], List[Tuple[str, int]]]:
    frequency = {}
    for sym in text:
        frequency[sym] = frequency.get(sym, 0) + 1

    if sort:
        return sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return frequency

#Частота біграм, які не перетинаються
def bigram_frequency_without_intersection(text: str) -> List[Tuple[str, int]]:
    letters_list = list(text)
    bigrams = [letters_list[i] + letters_list[i+1] for i in range(0, len(letters_list)-1, 2)]
    return symbol_frequency(bigrams, sort=True)

Key = Tuple[int, int]
System = Tuple[Tuple[int, int], Tuple[int, int]]
# Розв'язує систему з двох порівнянь та знаходить ймовірний ключ
def find_possible_key(system: System, module: int) -> List[Key]:
    x1, y1 = system[0]
    x2, y2 = system[1]
    a = solve_congruence((x1-x2, y1-y2, module))
    keys = []
    if a:
        for el in a:
            b = solve_congruence((1, y1-el*x1, module))
            if b:
                keys.append((el, b[0]))
        return keys
    return []

# Знаходить усі ймовірні ключі
def possible_keys_frequency_definer(ciphertext: str, lang_text: str='стнотонаен', alphabet: List[str]=alphabet) -> Set[Key]:
    top = 5
    top_bgs_in_lang = [pair[0] for pair in bigram_frequency_without_intersection(lang_text)[:top]]
    top_bgs_in_ciphertext = [pair[0] for pair in bigram_frequency_without_intersection(ciphertext)[:top]]

    module = len(alphabet) ** 2
    keys = []
    for i in range(top):
        for j in range(top):
            for k in range(top):
                if k != i: 
                    for l in range(top):
                        if l != j:
                            bg1, bg2 = bigram_to_num[top_bgs_in_lang[i]], bigram_to_num[top_bgs_in_lang[k]]
                            ct1, ct2 = bigram_to_num[top_bgs_in_ciphertext[j]], bigram_to_num[top_bgs_in_ciphertext[l]]
                            system = ((bg1, ct1), (bg2, ct2))
                            keys += find_possible_key(system, module)                  
    return set(keys)

some_forbidden_bigrams = ['аь', 'еь', 'иь', 'оь', 'уь', 'ыь', 'эь', 'юь', 'яь']
# Перевірка ключа
def is_key(plaintext: str, top_syms_in_lang: List[str], top: int, forbidden_bigrams: List[str]=some_forbidden_bigrams) -> bool:
    for bg in some_forbidden_bigrams: 
        if bg in plaintext:
            return False

    top_syms_in_plaintext = [pair[0] for pair in symbol_frequency(plaintext, sort=True)[:top]]
    return len([sym for sym in top_syms_in_lang if sym in top_syms_in_plaintext]) > top-2

# Аналізує отримані повідомлення та визначає точний ключ 
def key_definer(lang_text: str, ciphertext: str, alphabet: List[str]=alphabet) -> List[Key]:
    keys = []
    top = 5
    top_syms_in_lang = [pair[0] for pair in symbol_frequency(lang_text, sort=True)[:top]]
    for key in possible_keys_frequency_definer(ciphertext):
        plaintext = affine_decipher(ciphertext, key)
        if is_key(plaintext, top_syms_in_lang, top):
            keys.append(key)
    return keys
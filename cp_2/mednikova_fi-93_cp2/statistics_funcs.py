from typing import Dict, List, Tuple, Union
from vigenere_cipher_funcs import num_to_sym, sym_to_num, sym_amount

def symbol_frequency(text: str, sort: bool=False) -> Union[Dict[str, int], List[Tuple[str, int]]]:
    frequency = {}
    for sym in text:
        frequency[sym] = frequency.get(sym, 0) + 1

    if sort:
        return sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return frequency

def affinity_index(text: str) -> float:
    n = len(text)
    AI = 0
    for _, freq in symbol_frequency(text).items():
        AI += freq * (freq - 1)
    AI /= n * (n-1)    
    return AI

def ciphertext_to_blocks(ciphertext: str, blocks_amount: int) -> Dict[str, str]:
    blocks = {}
    for i in range(blocks_amount):
        blocks['Y{}'.format(i)] = ciphertext[i::blocks_amount]
    return blocks

def blocks_af_ind(ciphertext: str, blocks_amount: int) -> List[float]:
    return [affinity_index(block) for block in ciphertext_to_blocks(ciphertext, blocks_amount).values()]

def key_len_definer(ciphertext: str, theoretical_af_ind: float) -> int:
    key_len = 2
    while key_len < 30:
        af_inds_for_cipher = blocks_af_ind(ciphertext, key_len)
        af_ind = sum(af_inds_for_cipher) / len(af_inds_for_cipher)
    
        if round(af_ind, 3) - 0.005 <= round(theoretical_af_ind, 4) <= round(af_ind, 3) + 0.005:
            return key_len
        key_len += 1
    

def key_frequency_definer(lang_text: str, ciphertext: str, th_af_ind: int) -> str:
    key = ''
    key_len = key_len_definer(ciphertext, th_af_ind)
    top_letter_in_lang = symbol_frequency(lang_text, sort=True)[0][0]
    blocks = ciphertext_to_blocks(ciphertext, key_len)

    for i in range(key_len):
        top_letter_in_block = symbol_frequency(blocks['Y{}'.format(i)], sort=True)[0][0]
        key += num_to_sym[(sym_to_num[top_letter_in_block] - sym_to_num[top_letter_in_lang]) % sym_amount]
    return key

def g_definer(lang_freq: Dict[str, float], block: str) -> int:
    M_cur = {}
    for g in range(sym_amount):
        for t in range(sym_amount):
            M_cur[g] = M_cur.get(g, 0) + lang_freq[num_to_sym[t]] * symbol_frequency(block).get(num_to_sym[(t + g) % sym_amount], 0)

    cur_output = []
    for g in M_cur.values():
        cur_output.append(round(g, 1))

    g = [g for g, v in M_cur.items() if v == max(M_cur.values())][0]
    return g, cur_output

def key_M_definer(lang_text: str, ciphertext: str, th_af_ind: int) -> str:
    key = ''
    key_len = key_len_definer(ciphertext, th_af_ind)
    blocks = ciphertext_to_blocks(ciphertext, key_len)
    lang_freq = {letter: freq / sym_amount for letter, freq in symbol_frequency(lang_text).items()}
    
    table = []
    for i in range(key_len):
        temp = g_definer(lang_freq, blocks['Y{}'.format(i)])
        key += num_to_sym[temp[0]]
        table.append(temp[1])

    return key, table
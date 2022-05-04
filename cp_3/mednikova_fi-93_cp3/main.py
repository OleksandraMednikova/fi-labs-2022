from frequency.frequency_analysis import bigram_frequency_without_intersection, key_definer, possible_keys_frequency_definer
from text_getter.text_getter import text_getter
from cipher.affine_cipher import affine_cipher, affine_decipher

fname = 'txt/text_for_theor_freq.txt'
try:
    fhandle = open(fname)
except:
    print('File cannot be opened: ', fname)
    print('Default file will be used')
    fname = 'txt/text_for_theor_freq.txt'
    fhandle = open(fname)

text_for_theoretical_freq1 = text_getter(fhandle.read(), {'ъ': 'ь', 'ё': 'е'})
text_for_theoretical_freq2 = text_getter('стнотонаен')
theoretical_freq1 = bigram_frequency_without_intersection(text_for_theoretical_freq1)[:5]
theoretical_freq2 = bigram_frequency_without_intersection(text_for_theoretical_freq2)[:5]
fhandle.close()

fname = 'txt/ciphertext.txt'
try:
    fhandle = open(fname)
except:
    print('File cannot be opened: ', fname)
    print('Default file will be used')
    fname = 'txt/ciphertext.txt'
    fhandle = open(fname)

ciphertext = text_getter(fhandle.read())
ciphertext_freq = bigram_frequency_without_intersection(ciphertext)[:5]
fhandle.close()

for key in key_definer(text_for_theoretical_freq1, ciphertext):
    print(affine_decipher(ciphertext, key))
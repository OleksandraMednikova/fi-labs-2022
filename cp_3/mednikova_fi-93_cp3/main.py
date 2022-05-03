from frequency.frequency import bigram_frequency_without_intersection
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

text_for_theoretical_freq = text_getter(fhandle.read(), {'ъ': 'ь', 'ё': 'е'})
theoretical_freq = bigram_frequency_without_intersection(text_for_theoretical_freq)[:5]
fhandle.close()

fname = 'txt/test'
try:
    fhandle = open(fname)
except:
    print('File cannot be opened: ', fname)
    print('Default file will be used')
    fname = 'txt/test'
    fhandle = open(fname)

ciphertext = text_getter(fhandle.read())
ciphertext_freq = bigram_frequency_without_intersection(ciphertext)[:5]
fhandle.close()

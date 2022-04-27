from text_getter import text_getter
from vigenere_cipher_funcs import vigenere_cipher
from statistics_funcs import affinity_index, symbol_frequency

fname = 'plaintext.txt'
try:
    fhandle = open(fname)
except:
    print('File cannot be opened: ', fname)
    print('Default file will be used')
    fname = 'plaintext.txt'
    fhandle = open(fname)

raw_text = fhandle.read()
fhandle.close()

fname = 'plaintext_filtered.txt'
try:
    fhandle = open(fname, 'w')
except:
    print('File cannot be opened: ', fname, 'w')
    print('Default file will be used')
    fname = 'plaintext_filtered.txt'
    fhandle = open(fname)

text = text_getter(raw_text, {'ё': 'e'})
fhandle.write(text_getter(text, {'ё': 'e'}))
fhandle.close()

fhandle = open('plaintext_filtered.txt')
plaintext = fhandle.read()
fhandle.close()

fname = 'result.txt'
try:
    fhandle = open(fname, 'w')
except:
    print('File cannot be opened: ', fname, 'w')
    print('Default file will be used')
    fname = 'result.txt'
    fhandle = open(fname)

keys = ['оп', 'ршу', 'нгав', 'длвыц', 'мнгшпрнивы', 'йфронистыгш', 'ьтдюбчяыцнзх', 
        'панроаааэжхйф', 'умгшровлыффолл', 'зоежлемионлрока', 'каваарйжееанкосо', 'пдшакуоюжжэсьлеыв', 
        'йцывввффычнссимтъх', 'рвоарлтшсщтлыфзххзч', 'йгнушйячтлдфыоароывы']

fhandle.write('-' * 10)
fhandle.write('\nЗАВДАННЯ 1\n')
fhandle.write('-' * 10)
fhandle.write('\nВихідне повідомлення (ВП): {} \n'.format(plaintext))
ciphertexts = {len(key): vigenere_cipher(plaintext, key) for key in keys}
for key_len, cipher in ciphertexts.items():
    fhandle.write('Отриманий шифротекст(ШТ) при довжині ключа = {}: {} \n'.format(key_len, cipher))

fhandle.write('\n'+ ('-' * 10))
fhandle.write('\nЗАВДАННЯ 2\n')
fhandle.write('-' * 10)
f2name = 'text_for_theoretical_affinity_index.txt'
try:
    f2handle = open(f2name)
except:
    print('File cannot be opened: ', f2name)
    print('Default file will be used')
    f2name = 'text_for_theoretical_affinity_index.txt'
    f2handle = open(f2name)
fhandle.write('\nТеоретичний індекс відповідності: {:.5f} \n'.format(affinity_index(f2handle.read())))
f2handle.close()
fhandle.write('Індекс відповідності ВП: {:.5f} \n'.format(affinity_index(plaintext)))
affinity_inds = {len(key): affinity_index(ciphertexts[len(key)]) for key in keys}
for key_len, af_ind in affinity_inds.items():
    fhandle.write('Індекс відповідності ШТ при довжині ключа = {}: {:.5f} \n'.format(key_len, af_ind))

fhandle.close()


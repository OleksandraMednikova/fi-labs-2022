from text_getter import text_getter
from vigenere_cipher_funcs import vigenere_cipher, vigenere_decipher
from statistics_funcs import affinity_index, key_M_definer, key_frequency_definer, key_len_definer

fname = 'txt/plaintext.txt'
try:
    fhandle = open(fname)
except:
    print('File cannot be opened: ', fname)
    print('Default file will be used')
    fname = 'txt/plaintext.txt'
    fhandle = open(fname)

raw_text = fhandle.read()
fhandle.close()

fname = 'txt/plaintext_filtered.txt'
try:
    fhandle = open(fname, 'w')
except:
    print('File cannot be opened: ', fname, 'w')
    print('Default file will be used')
    fname = 'txt/plaintext_filtered.txt'
    fhandle = open(fname)

text = text_getter(raw_text, {'ё': 'e'})
fhandle.write(text_getter(text, {'ё': 'e'}))
fhandle.close()

fhandle = open('txt/plaintext_filtered.txt')
plaintext = fhandle.read()
fhandle.close()

fname = 'txt/result.txt'
try:
    fhandle = open(fname, 'w')
except:
    print('File cannot be opened: ', fname, 'w')
    print('Default file will be used')
    fname = 'txt/result.txt'
    fhandle = open(fname)

keys = ['оп', 'ршу', 'нгав', 'длвыц', 'мнгшпрнивы', 'йфронистыгш', 'ьтдюбчяыцнзх', 
        'панроаааэжхйф', 'умгшровлыффолл', 'зоежлемионлрока', 'каваарйжееанкосо', 'пдшакуоюжжэсьлеыв', 
        'йцывввффычнссимтъх', 'рвоарлтшсщтлыфзххзч', 'йгнушйячтлдфыоароывы']

fhandle.write('-' * 10)
fhandle.write('\nЗАВДАННЯ 1\n')
fhandle.write('-' * 10)
fhandle.write('\nВихідне повідомлення (ВП): {} \n'.format(plaintext))
ciphertexts = {key: vigenere_cipher(plaintext, key) for key in keys}
for key, cipher in ciphertexts.items():
    fhandle.write('Отриманий шифротекст(ШТ) при довжині ключа = {}: {} \n'.format(len(key), cipher))

fhandle.write('\n'+ ('-' * 10))
fhandle.write('\nЗАВДАННЯ 2\n')
fhandle.write('-' * 10)
f2name = 'txt/text_for_theoretical_affinity_index.txt'
try:
    f2handle = open(f2name)
except:
    print('File cannot be opened: ', f2name)
    print('Default file will be used')
    f2name = 'txt/text_for_theoretical_affinity_index.txt'
    f2handle = open(f2name)
text_for_theoretical_af_ind = text_getter(f2handle.read(), {'ё': 'е'})
theoretical_af_ind = affinity_index(text_for_theoretical_af_ind)
fhandle.write('\nТеоретичний індекс відповідності: {:.5f} \n'.format(theoretical_af_ind))
f2handle.close()
fhandle.write('Індекс відповідності ВП: {:.5f} \n'.format(affinity_index(plaintext)))
affinity_inds = {item[0]: affinity_index(item[1]) for item in ciphertexts.items()}
for key, af_ind in affinity_inds.items():
    fhandle.write('Індекс відповідності ШТ при довжині ключа = {}: {:.5f} \n'.format(len(key), af_ind))

fhandle.write('\n'+ ('-' * 10))
fhandle.write('\nЗАВДАННЯ 3\n')
fhandle.write('-' * 10)
f3name = 'txt/ciphertext.txt'
try:
    f3handle = open(f3name)
except:
    print('File cannot be opened: ', f3name)
    print('Default file will be used')
    f3name = 'txt/ciphertext.txt'
    f3handle = open(f3name)
ciphertext = f3handle.read()
f3handle.close()
key_len = key_len_definer(ciphertext, theoretical_af_ind)
fhandle.write('\nДовжина ключа: {} \n'.format(key_len))
key = key_frequency_definer(text_for_theoretical_af_ind, ciphertext, theoretical_af_ind)
fhandle.write('Ключ, знайдений за допомогою найчастіших літер: {}\n'.format(key))
fhandle.write('Текст, отриманий з ШТ з ключем {}: {}\n'.format(key, vigenere_decipher(ciphertext, key)[:200]))
key = 'чугунныенебеса'
fhandle.write('Відкорегований ключ: {}\n'.format(key))
fhandle.write('Текст, отриманий з ШТ з ключем {}: {}\n'.format(key, vigenere_decipher(ciphertext, key)[:200]))
key = key_M_definer(text_for_theoretical_af_ind, ciphertext, theoretical_af_ind)
fhandle.write('Ключ, знайдений за допомогою функції M_i(g): {}\n'.format(key))
fhandle.write('Текст, отриманий з ШТ з ключем {}: {}\n'.format(key, vigenere_decipher(ciphertext, key)[:200]))
fhandle.close()
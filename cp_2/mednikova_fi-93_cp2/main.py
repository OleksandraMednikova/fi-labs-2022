from text_getter import text_getter
from vigenere_cipher_funcs import vigenere_cipher

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

KEY2 = 'оп'
KEY3 = 'ршу'
KEY4 = 'нгав'
KEY5 = 'длвыц'
KEY10 = 'мнгшпрнивы'
KEY11 = 'йфронистыгш'
KEY12 = 'ьтдюбчяыцнзх'
KEY13 = 'панроаааэжхйф'
KEY14 = 'умгшровлыффолл'
KEY15 = 'зоежлемионлрока'
KEY16 = 'каваарйжееанкосо'
KEY17 = 'пдшакуоюжжэсьлеыв'
KEY18 = 'йцывввффычнссимтъх'
KEY19 = 'рвоарлтшсщтлыфзххзч'
KEY20 = 'йгнушйячтлдфыоароывы'

fname = 'result.txt'
try:
    fhandle = open(fname, 'w')
except:
    print('File cannot be opened: ', fname, 'w')
    print('Default file will be used')
    fname = 'result.txt'
    fhandle = open(fname)

fhandle.write('ЗАВДАННЯ 1\n\n')
fhandle.write('Вихідне повідомлення: {} \n'.format(plaintext))
fhandle.write('Отриманий шифротекст при довжині ключа = 2: {} \n'.format(vigenere_cipher(text, KEY2)))
fhandle.write('Отриманий шифротекст при довжині ключа = 3: {} \n'.format(vigenere_cipher(text, KEY3)))
fhandle.write('Отриманий шифротекст при довжині ключа = 4: {} \n'.format(vigenere_cipher(text, KEY4)))
fhandle.write('Отриманий шифротекст при довжині ключа = 5: {} \n'.format(vigenere_cipher(text, KEY5)))
fhandle.write('Отриманий шифротекст при довжині ключа = 10: {} \n'.format(vigenere_cipher(text, KEY10)))
fhandle.write('Отриманий шифротекст при довжині ключа = 11: {} \n'.format(vigenere_cipher(text, KEY11)))
fhandle.write('Отриманий шифротекст при довжині ключа = 12: {} \n'.format(vigenere_cipher(text, KEY12)))
fhandle.write('Отриманий шифротекст при довжині ключа = 13: {} \n'.format(vigenere_cipher(text, KEY13)))
fhandle.write('Отриманий шифротекст при довжині ключа = 14: {} \n'.format(vigenere_cipher(text, KEY14)))
fhandle.write('Отриманий шифротекст при довжині ключа = 15: {} \n'.format(vigenere_cipher(text, KEY15)))
fhandle.write('Отриманий шифротекст при довжині ключа = 16: {} \n'.format(vigenere_cipher(text, KEY16)))
fhandle.write('Отриманий шифротекст при довжині ключа = 17: {} \n'.format(vigenere_cipher(text, KEY17)))
fhandle.write('Отриманий шифротекст при довжині ключа = 18: {} \n'.format(vigenere_cipher(text, KEY18)))
fhandle.write('Отриманий шифротекст при довжині ключа = 19: {} \n'.format(vigenere_cipher(text, KEY19)))
fhandle.write('Отриманий шифротекст при довжині ключа = 20: {} \n'.format(vigenere_cipher(text, KEY20)))
fhandle.close()

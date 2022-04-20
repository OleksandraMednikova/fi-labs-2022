import entropy_funcs
from text_getter import text_getter, alphabet

fname = 'text.txt'
try:
    fhandle = open(fname)
except:
    print('File cannot be opened: ', fname)
    print('Default file will be used')
    fname = 'text.txt'
    fhandle = open(fname)

raw_text = fhandle.read()
fhandle.close()

text = text_getter(raw_text, alphabet + [' '])

fname = 'result.txt'
try:
    fhandle = open(fname, 'w')
except:
    print('File cannot be opened: ', fname, 'w')
    print('Default file will be used')
    fname = 'result.txt'
    fhandle = open(fname)

fhandle.write('\nЧАСТОТА БУКВ У ТЕКСТІ З ПРОБІЛОМ:\n')
for line in entropy_funcs.letter_frequency(text):
    fhandle.write(str(line) + '\n')
fhandle.write('\nЧАСТОТА БІГРАМ БЕЗ ПЕРЕТИНУ У ТЕКСТІ З ПРОБІЛОМ:\n')
for line in entropy_funcs.bigram_frequency_without_intersection(text):
    fhandle.write(str(line) + '\n')
fhandle.write('\nЧАСТОТА БІГРАМ З ПЕРЕТИНОМ У ТЕКСТІ З ПРОБІЛОМ:\n')
for line in entropy_funcs.bigram_frequency_with_intersection(text):
    fhandle.write(str(line) + '\n')
fhandle.write('\nH_1 У ТЕКСТІ З ПРОБІЛОМ: ')
fhandle.write(str(entropy_funcs.n_gram_entropy(entropy_funcs.letter_frequency(text), 1)))
fhandle.write('\nH_2 БІГРАМ БЕЗ ПЕРЕТИНУ У ТЕКСТІ З ПРОБІЛОМ: ')
fhandle.write(str(entropy_funcs.n_gram_entropy(entropy_funcs.bigram_frequency_without_intersection(text), 2)))
fhandle.write('\nH_2 БІГРАМ З ПЕРЕТИНОМ У ТЕКСТІ З ПРОБІЛОМ: ')
fhandle.write(str(entropy_funcs.n_gram_entropy(entropy_funcs.bigram_frequency_with_intersection(text), 2)))

fhandle.write('\n' + '-' * 100)

text = text_getter(raw_text)
fhandle.write('\nЧАСТОТА БУКВ У ТЕКСТІ БЕЗ ПРОБІЛУ:\n')
for line in entropy_funcs.letter_frequency(text):
    fhandle.write(str(line) + '\n')
fhandle.write('\nЧАСТОТА БІГРАМ БЕЗ ПЕРЕТИНУ У ТЕКСТІ БЕЗ ПРОБІЛУ:\n')
for line in entropy_funcs.bigram_frequency_without_intersection(text):
    fhandle.write(str(line) + '\n')
fhandle.write('\nЧАСТОТА БІГРАМ З ПЕРЕТИНОМ У ТЕКСТІ БЕЗ ПРОБІЛУ:\n')
for line in entropy_funcs.bigram_frequency_with_intersection(text):
    fhandle.write(str(line) + '\n')
fhandle.write('\nH_1 У ТЕКСТІ БЕЗ ПРОБІЛУ: ')
fhandle.write(str(entropy_funcs.n_gram_entropy(entropy_funcs.letter_frequency(text), 1)))
fhandle.write('\nH_2 БІГРАМ БЕЗ ПЕРЕТИНУ У ТЕКСТІ БЕЗ ПРОБІЛУ: ')
fhandle.write(str(entropy_funcs.n_gram_entropy(entropy_funcs.bigram_frequency_without_intersection(text), 2)))
fhandle.write('\nH_2 БІГРАМ З ПЕРЕТИНОМ У ТЕКСТІ БЕЗ ПРОБІЛУ: ')
fhandle.write(str(entropy_funcs.n_gram_entropy(entropy_funcs.bigram_frequency_with_intersection(text), 2)))
fhandle.close()
from typing import List

#Можна додати або видалити символ(и) за потребою
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 
            'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 
            'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']

def text_getter(text:str, alphabet:List = alphabet) -> str:
    text = text.lower()

    dellist = set(symbol for symbol in text if symbol not in alphabet)
    for symbol in dellist:
        text = text.replace(symbol, '')
    text = ' '.join(text.split())

    return text
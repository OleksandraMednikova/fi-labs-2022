from typing import List, Tuple, Union, Dict
import math

#Підрахунок кількості потрібних частинок у тексті
def frequency_definer(parts: Union[str, List]) -> Dict:
    frequency = {}
    for part in parts:
        frequency[part] = frequency.get(part, 0) + 1

    parts_amount = len(parts)
    for part, amount in frequency.items():
        frequency[part] = amount / parts_amount 
    return frequency

#Сортування даних про частоту
def frequency_sort(data: Dict) -> List[Tuple[str, int]]:
    return sorted(data.items(), key=lambda item: item[1], reverse=True)

#Частота літер
def letter_frequency(text: str) -> List[Tuple[str, int]]:
    return frequency_sort(frequency_definer(text))

#Частота біграм, які не перетинаються
def bigram_frequency_without_intersection(text: str) -> List[Tuple[str, int]]:
    letters_list = list(text)
    bigrams = [letters_list[i] + letters_list[i+1] for i in range(0, len(letters_list)-1, 2)]
    return frequency_sort(frequency_definer(bigrams))

#Частота біграм, які перетинаються
def bigram_frequency_with_intersection(text: str) -> List[Tuple[str, int]]:
    letters_list = list(text)
    bigrams = [letters_list[i] + letters_list[i+1] for i in range(len(letters_list)-1)]

    return frequency_sort(frequency_definer(bigrams))

#Питома ентропія на символ n-грами
def n_gram_entropy(frequency: List[Tuple[str, int]], n:int) -> float:
    entropy = 0
    for _, freq in frequency:
        entropy += freq * math.log2(freq)

    return -1 / n * entropy


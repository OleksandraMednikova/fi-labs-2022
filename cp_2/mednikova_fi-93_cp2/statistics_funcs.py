from typing import Dict

def symbol_frequency(text: str) -> Dict[str, int]:
    frequency = {}
    for sym in text:
        frequency[sym] = frequency.get(sym, 0) + 1
    return frequency

def affinity_index(text: str) -> float:
    n = len(text)
    AI = 0
    for _, freq in symbol_frequency(text).items():
        AI += freq * (freq - 1)
    AI /= n * (n-1)    
    return AI
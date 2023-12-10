from typing import List

def get_user_words() -> List[str]:
    words = []
    while True:
        word = input('Digite a palavra: ')
        if word == '0':
            break
        words.append(word)
    return words

# A função "get_user_words" é uma função pura. Ela sempre terá o mesmo resultado com os mesmos Inputs
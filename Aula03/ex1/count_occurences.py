import typing
from get_words import get_user_words

all_letters = ''.join(get_user_words())



def count_x_occurences(word: str) -> float:
    occur = 0
    length_list = len(word)
    for letter in word:
        if letter == 'x'.lower():
            occur += 1
    result = occur / length_list
    print(length_list, occur)
    return result

# A função "count_x_occurences" é uma função pura. Ela sempre terá o mesmo resultado com os mesmos Inputs


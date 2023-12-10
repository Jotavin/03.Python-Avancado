from typing import List
from count_occurences import count_x_occurences, all_letters

result = count_x_occurences(all_letters)

def inform_average(average: float) -> None:
    print(f'{average:.3f}')

inform_average(result)

# A função "inform_average" é uma função pura. Ela sempre terá o mesmo resultado com os mesmos Inputs

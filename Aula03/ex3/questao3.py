from typing import Union
from math import sqrt
def bhaskara(a: int, b: float, c: Union[int, float] ) -> float:
    x1, x2 = 0, 0
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print('Delta negativo. Não existem raízes reais.')
        return
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'Primeira raiz: {x1:.2f}\nSegunda raiz: {x2:.2f}')

bhaskara(2, -16, -18)
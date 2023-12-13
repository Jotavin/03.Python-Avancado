from typing import List

class Celular:
    def __init__(self, nome: str, preco: int):
        self.nome = nome
        self.preco = preco

def verificar_celulares(lista: List[Celular]) -> int:
    total = sum(Celular.preco for Celular in lista)
    return total


lista_celulares = [
    Celular('A1', 1000),
    Celular('A3', 1500),
    Celular('A6', 2000),
    Celular('A10', 2500),
    #Tenis('Vento1', 999)
]

resultado = verificar_celulares(lista_celulares)
print(f'Total R${resultado}')
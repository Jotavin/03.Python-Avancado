import time
import sys
start_time = time.time() 
def create_list(n):          # Função com loop com for convencional, possui um tempo menor de execução e maior uso de memória.
    list = []
    for i in range(n):
        list.append(i)
    return list

# def create_list(n):         # Função com "yield", possui menor tempo de execução e menor uso de memória.
#     for i in range(n):
#         yield i

list = create_list(1_000_000)
print('Memoria utilizada: ', sys.getsizeof(list))

end_time = time.time()
print(f'Tempo decorrido sem "yield": {end_time - start_time}s')

# A screenshot enviada possui 2 tempos no termional. O primeiro é referente a função usando o "yield" e a segunda sem. A com "yield" é mais rápida.
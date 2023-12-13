import time
import sys
start_time = time.time() 

# def create_list(n):                      # List Comprehension
#     return [x ** 2 for x in range(n)]


def create_list(n):                        # Função com "yield" (Generator).
    for i in range(n):
        yield i ** 2


list = create_list(5)

for i in list:
    print(i)

print('Memoria utilizada: ', sys.getsizeof(list))

end_time = time.time()
print(f'Tempo decorrido com "yield": {end_time - start_time}s')
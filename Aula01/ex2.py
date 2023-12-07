def sum(a, b):
    print(a + b)


fruit_list = []
def add_list():
    fruit = input('Adicionar fruta: ')
    global fruit_list
    fruit_list.append(fruit)

sum(5,2)

print(fruit_list)
add_list()
print(fruit_list)

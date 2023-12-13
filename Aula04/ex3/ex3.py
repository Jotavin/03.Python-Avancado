# Iterador é um protocolo de um objeto utiliza. O diferencial desse "iterador" é que ele mantém o estado quando está sendo iterado, e também guarda até qual elemento que foi   percorrido para, então, conseguir acessar o próximo com o __next__().

# Um exemplo prático e simples ao criar um objeto iterador é utilizando o __iter__():
a = ['a', 'b', 'c', 'd']
b = iter(a)
for letra in b:
    print(letra)
pessoa = 'Paulo'
print(pessoa)

def change_name(s):
    global pessoa
    nome = s
    sobrenome = input('Digite o sobrenome: ')
    pessoa = f'{nome} {sobrenome}'.title()
    return pessoa.title()

change_name(pessoa)

print(pessoa)

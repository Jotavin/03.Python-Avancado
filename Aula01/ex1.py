import random


def greetings():
    print('Bem-vindo(a) ao curso de Python!')

def new_greetings(name, age=18):
    greetings()
    print(f'{name}, {age} anos')


def cadastro(nome, endereco, cep, idade=18):
    new_greetings(nome, idade)
    name = nome
    addres = endereco
    Cep = cep
    age = idade
    turma = 'PY-2024-001'
    matricula = f'{(random.random() * 1_000_000):.0f}'
    return name, turma, matricula

nome = input('Nome: ')
endereco = input('Endereço: ')
cep = input('Código CEP: ')
idade = input('Idade: ')

novo_nome, matricula, turma = cadastro(nome, endereco, cep, idade)

print(f'Olá {novo_nome}, sua matrícula é {matricula} na turma {turma}')




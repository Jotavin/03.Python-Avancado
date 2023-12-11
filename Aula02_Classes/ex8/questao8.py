lista_livros = []
def cadastrar_livro(titulo, autor, ano) -> dict:
    global lista_livros
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    lista_livros.append(livro)
    return livro


def abnt(livro):
    autor_final = ''
    ultimo_espaco = livro["autor"].rfind(' ') + 1
    ultimo_nome = livro["autor"][ultimo_espaco:].upper().replace('.', '')
    autor_final = ultimo_nome + ', '
    letras_nome = livro["autor"][:ultimo_espaco]
    lista_nome = letras_nome.split()

    for nome in lista_nome:
        autor_final += nome[:1].upper() + '. '
    
    return autor_final


def listar_livros():
    global lista_livros
    for livro in lista_livros:
        print(f'O livro "{livro["titulo"]}" foi escrito por {livro["autor"]} em {livro["ano"]}')



sherlock = cadastrar_livro('O Cão dos Baskervilles', 'Arthur C. Doyle', '1902')

jogos_vorazes = cadastrar_livro('Jogos Vorazes', 'Suzanne Collins', '2012')

alasca = cadastrar_livro('Quem é você, Alasca?', 'John Green', '2005')

harry_potter = cadastrar_livro('Harry Potter e o Enigma do Príncipe', 'J. K. Rowling', '2005')

# print(lista_livros)
def pesquisar_autor(nome_autor):
    for livro in lista_livros:
        nome = livro['autor']
        if nome == nome_autor:
            return f'O(A) autor(a) {nome_autor} escreveu o livro {livro["titulo"]}'
# print(pesquisar_autor('J. K. Rowling'))
def menu_principal():
    print('1-Cadastrar Livro')
    print('2-Listar Livros')
    print('3-Pesquisar por Autor')
    print('4-Sair')
    escolha = int(input('Digite sua opção desejada: '))
    
    if escolha == 1:
        nome = input('Digite o nome do livro: ')
        autor = input('Digite o autor do livro: ')
        ano = input('Digite o ano de lançamento do livro: ')
        return cadastrar_livro(nome, autor, ano)

    elif escolha == 2:
        return listar_livros()

    elif escolha == 3:
        autor = input('Digite o autor do livro: ')
        return pesquisar_autor(autor)
    

# print(menu_principal())
# print(sherlock["titulo"])
# print(abnt(harry_potter))
# listar_livros()


def sub_menu1():
    print('1-Cadastrar Livro')
    print('2-Listar Livros')
    print('3-Pesquisar por Autor')
    print('4-Listar Livros em Inglês')
    print('5-Sair')
    escolha = int(input('Digite sua opção desejada: '))

    while True:

        if escolha == 1:
            nome = input('Digite o nome do livro: ')
            autor = input('Digite o autor do livro: ')
            ano = input('Digite o ano de lançamento do livro: ')
            return cadastrar_livro(nome, autor, ano)

        elif escolha == 2:
            return listar_livros()

        elif escolha == 3:
            autor = input('Digite o autor do livro: ')
            return pesquisar_autor(autor)
        
        elif escolha == 4:
            return 'Opção 4 escolhida!'
        
        else:
            print('\nDigite um valor de menu válido')
            sub_menu1()

print(sub_menu1())
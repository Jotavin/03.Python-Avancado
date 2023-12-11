class Livro():
    def __init__(self, titulo: str, autor: str, ano: str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    

    def cadastrar_livro(self) -> dict:
        return {self.titulo: {"autor": self.autor, "ano": self.ano}}
    

    def abnt(self):
        autor_final = ''
        ultimo_espaco = self.autor.rfind(' ') + 1
        ultimo_nome = self.autor[ultimo_espaco:].upper().replace('.', '')
        autor_final = ultimo_nome + ', '
        letras_nome = self.autor[:ultimo_espaco]
        lista_nome = letras_nome.split()

        for nome in lista_nome:
            autor_final += nome[:1].upper() + '. '
        
        return autor_final


def listar_livros(*lista_livros):
    lista = []
    for livro in lista_livros:
        lista.append(livro)
    
    for livro in lista:
        print(f'O livro "{livro.titulo}" foi escrito por {livro.autor} em {livro.ano}')



sherlock = Livro('O Cão dos Baskervilles', 'Arthur C. Doyle', '1902')
jogos_vorazes = Livro('Jogos Vorazes', 'Suzanne Collins', '2012')
alasca = Livro('Quem é você, Alasca?', 'John Green', '2005')
harry_potter = Livro('Harry Potter e o Enigma do Príncipe', 'J. K. Rowling', '2005')

# listar_livros(sherlock, jogos_vorazes, alasca, harry_potter)

print(sherlock.abnt())
print(jogos_vorazes.abnt())
print(alasca.abnt())
print(harry_potter.abnt())
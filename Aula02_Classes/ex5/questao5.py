class Livro():
    def __init__(self, titulo: str, autor: str, ano: str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def cadastrar_livro(self) -> dict:
        return {self.titulo: {"autor": self.autor, "ano": self.ano}}
    

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

listar_livros(sherlock, jogos_vorazes, alasca, harry_potter)
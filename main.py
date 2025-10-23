

class Livro:

    def __init__(self, titulo, autor, estilo ):
        self.titulo = titulo
        self.autor = autor
        self.estilo = estilo

    def mostrar_livro(self):
        print(f'Livro: {self.titulo} Autor: {self.autor} Estilo: {self.estilo}')

class Biblioteca:

    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'O livro: {livro} foi adicionado a biblioteca!')

    def remover_livro(self,livro):
        self.livros.remove(livro)
        print(f'O livro: {livro} foi removido!')

    def listar_livros(self):
        print('Esta é a lista de livros:')
        for livro in self.livros:
            print(livro.mostrar_livro())




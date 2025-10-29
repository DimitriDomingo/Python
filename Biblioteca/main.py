

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
        print(f'O livro: {livro.titulo} foi adicionado a biblioteca!')

    def remover_livro(self,livro):
        self.livros.remove(livro)
        print(f'O livro: {livro} foi removido!')

    def listar_livros(self):
        print('Esta é a lista de livros:')
        for livro in self.livros:
            livro.mostrar_livro()

def menu_interativo(biblioteca):
    while True:
        print('-=' * 15)
        print('1) Adicionar livros.')
        print('2) remover livro.')
        print('3) Listar livros.')
        print('4) Encerrar.')
        print('-=' * 15)

        opcao = int(input('Digite o número da operação que deseja fazer: '))

        if opcao == 1:
            livro = input('Livro: ')
            autor = input('Autor: ')
            estilo = input('Estilo: ')

            novo_livro = Livro(livro, autor, estilo)
            biblioteca.adicionar_livro(novo_livro)

        elif opcao == 2:
            titulo = input('Livro: ')
            livro_encontrado = None
            for livro in biblioteca.livros:
                if livro.titulo == titulo:
                    print('Livro encontrado!')
                    livro_encontrado = titulo
                    break
                if livro_encontrado:
                    biblioteca.remover_livro(livro_encontrado)

            biblioteca.remover_livro()

        elif opcao == 3:
            biblioteca.listar_livros()

        else:
            break

biblioteca = Biblioteca()
menu_interativo(biblioteca)
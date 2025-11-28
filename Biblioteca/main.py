import sqlite3

    # Classe Livro

class Livro:
    def __init__(self, titulo, autor, estilo ):
        self.titulo = titulo
        self.autor = autor
        self.estilo = estilo

    # Classe Cliente
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    #Classe BibliotecaDB
class BibliotecaDB:

    def __init__(self, nome_banco = "biblioteca.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo  TEXT NOT NULL,
        autor TEXT NOT NULL,
        estilo TEXT NOT NULL
        )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
        )""")

    # Métodos para livros

    def adicionar_livro(self, livro: Livro):
        self.cursor.execute("INSERT INTO livros (titulo, autor, estilo) VALUES (?, ?, ?)",
                            (livro.titulo, livro.autor, livro.estilo))
        self.conexao.commit()
        print(f'O livro "{livro.titulo}" foi adicionado!')

    def remover_livro(self,titulo):
        self.cursor.execute("DELETE FROM livros WHERE titulo = ?",
                            (titulo,))
        self.conexao.commit()
        print(f'O livro"{titulo}" foi removido!')

    def listar_livros(self):
        self.cursor.execute("SELECT * FROM livros")
        livros = self.cursor.fetchall()
        if not livros:
            print('A biblioteca está vazia.')
        else:
            print("Lista de livros")
            for livro in livros:
                print(f'ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Estilo: {livro[3]}')

    # Métodos para clientes

    def adicionar_cliente(self, cliente: Cliente):
        self.cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)",
                            (cliente.nome, cliente.email))
        self.conexao.commit()
        print(f'Cliente "{cliente}" foi cadastrado!')

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        clientes = self.cursor.fetchall()
        if not clientes:
            print('Não há nem um cliente cadastrado.')
        else:
            print('Lista de clientes')
            for cliente in clientes:
                print(f'ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}')

    # Criação do menu interativo

def menu_interativo(biblioteca):
    while True:
        print('-=' * 15)
        print('1) Adicionar livros')
        print('2) remover livro')
        print('3) Listar livros')
        print('4) Adicionar cliente')
        print('5) Listar clientes')
        print('6) Encerrar')
        print('-=' * 15)

        opcao = int(input('Digite o número da operação: '))

        if opcao == 1:
            livro = input('Titulo: ')
            autor = input('Autor: ')
            estilo = input('Estilo: ')

            novo_livro = Livro(livro, autor, estilo)
            biblioteca.adicionar_livro(novo_livro)

        elif opcao == 2:
            titulo = input('Livro: ')
            biblioteca.remover_livro(titulo)

        elif opcao == 3:
            biblioteca.listar_livros()

        elif opcao == 4:
            nome = input('Nome do cliente: ')
            email = input('Email do cliente: ')
            biblioteca.adicionar_clientes(nome, email)

        elif opcao == 5:
            biblioteca.listar_clientes()

        elif opcao == 6:
            print('Encerrando o prorama ...')
            break

        else:
            print('Opção inválida. Tente naovamente.')

biblioteca = BibliotecaDB()
menu_interativo(biblioteca)
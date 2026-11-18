#Exercício 5 – Sistema de Gestão de Biblioteca
class Livro:
    def __init__(self,titulo,isbn,estado):
        self.titulo = titulo
        self.isbn = isbn
        self.estado = estado

    def apresentar(self):
        print("titulo:", self.titulo)
        print("isbn:", self.isbn)
        print("estado:", self.estado)

    def emprestar(self):
        if self.estado == "disponivel":
            self.estado = "emprestado"
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")

    def devolver(self):
        if self.estado == "emprestado":
            self.estado = "disponivel"
            print(f"O livro '{self.titulo}' foi devolvido com sucesso.")


#livros,
print("\nLivros disponíveis na biblioteca:")
livro1 = Livro("Bíblia", "978-0261102385", "disponivel") 
livro2 = Livro("O Senhor dos Anéis", "978-0261102385", "disponivel")
livro3 = Livro("Harry Potter e a Pedra Filosofal", "978-0261102385", "disponivel")  
livro4 = Livro("O Pequeno Príncipe", "978-0261102385", "disponivel")

#emprestar livros
livro2.emprestar()
livro4.emprestar()
livro2.emprestar()

#devolver livros
livro4.devolver()

#apretação dos livros

livro1.apresentar()
livro2.apresentar()
livro3.apresentar()
livro4.apresentar()
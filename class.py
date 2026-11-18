class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
       

    def apresentar(self):
        print("nome:", self.nome)
        print("idade:", self.idade)
        print("curso:", self.curso)

#criar um objeto da classe aluno
aluno1 = Aluno("Eurico", 20, "Engenharia")
aluno2 = Aluno("João", 22, "Medicina")
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
curso = input("Digite o curso do aluno: ")
aluno3 = Aluno(nome, idade, curso)
#
aluno1.apresentar()
aluno2.apresentar()
aluno3.apresentar()
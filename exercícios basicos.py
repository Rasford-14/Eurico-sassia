class Estudante:
    def __init__(self, nome, numero_da_matricula, idade, curso):
        self.nome = nome
        self.numero_da_matricula = numero_da_matricula
        self.idade = idade
        self.curso = curso

    def apresentar(self):
     print("Nome:", self.nome)
     print("Número da matrícula:", self.numero_da_matricula)     
     print("Idade:", self.idade)
     print("Curso:", self.curso)

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso}.")

    #criar um objeto da classe aluno
aluno1 = Estudante("Eurico", 2023, 20, "Engenharia")
aluno2 = Estudante("João", 2212, 22, "Medicina")
nome = input("Digite o nome do aluno: ")
numero_da_matricula = int(input("Digite o número da matrícula do aluno: "))
idade = int(input("Digite a idade do aluno: "))
curso = input("Digite o curso do aluno: ")
aluno3 = Estudante(nome, numero_da_matricula, idade, curso)

#chamar os métodos dos objetos  
aluno1.apresentar()
aluno1.estudar()    
aluno2.apresentar()
aluno2.estudar()
aluno3.apresentar()
aluno3.estudar()
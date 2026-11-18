#Exercício 4 – Sistema de Gestão de Funcionários

class Funcionario:
    def __init__(self,nome,numero_de_identificacao,cargo,salario):
        self.nome = nome
        self.numero_de_identificacao = numero_de_identificacao
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        print("nome:", self.nome)
        print("numero_de_identificacao:", self.numero_de_identificacao)
        print("cargo:", self.cargo)
        print("salario:", self.salario)

    def aumentar_salario(self,percentual):
            
            aumento = self.salario * (percentual / 100)
            self.salario += aumento
            print(f"Salário de {self.nome} aumentado em {percentual}% para {self.salario:.2f}kz.")

    def calcular_salario_anual(self):
        salario_anual = self.salario * 12
        return salario_anual

#funcionarios
funcionario1 = Funcionario("João", 123, "Analista", 1000.00)
funcionario2 = Funcionario("Eurico", 456, "Gerente", 2000.00)
funcionario3 = Funcionario("Maria", 789, "Assistente", 800.00)

#seus dados
funcionario1.apresentar()   
funcionario2.apresentar()   
funcionario3.apresentar()

#fucionarios com aumento de salario
funcionario1.aumentar_salario(10)

#sálario anual
funcinario1_salario_anual = funcionario1.calcular_salario_anual()
print(f"Salário anual de {funcionario1.nome}: {funcinario1_salario_anual:.2f}kz")

funcionario2_salario_anual=funcionario2.calcular_salario_anual()
print(f"Salário anual de {funcionario2.nome}: {funcionario2_salario_anual:.2f}kz")

funcionario3_salario_anual=funcionario3.calcular_salario_anual()
print(f"Salário anual de {funcionario3.nome}: {funcionario3_salario_anual:.2f}kz")

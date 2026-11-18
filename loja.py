class Produto:
    def __init__(self, nome,codigo , preco , quantidade_em_estoque ):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque  

    def apresentar(self):
        print("nome:", self.nome)
        print("codigo:", self.codigo)
        print("preco:", self.preco)
        print("quantidade_em_estoque:", self.quantidade_em_estoque)

    def calcular_valor_total_estoque(self):
        return self.preco * self.quantidade_em_estoque
    def repor_estoque(self, quantidade):
        self.quantidade_em_estoque += quantidade
        print(f"Novo estoque de {self.nome}: {self.quantidade_em_estoque}")

#criar um objeto da classe produto
produto1 = Produto("Camiseta", 101, 29.99, 50)
produto2 = Produto("Calça", 102, 59.99, 30)
#ivocar os métodos dos objetos
produto1.apresentar()
valor_total_estoque1 = produto1.calucular_valor_total_estoque()
print(f"Valor total em estoque para {produto1.nome}: {valor_total_estoque1:.2f}kz")
produto1.repor_estoque(20)
produto2.apresentar()
valor_total_estoque2 = produto2.calucular_valor_total_estoque()
print(f"Valor total em estoque para {produto2.nome}: {valor_total_estoque2:.2f}kz")

produto2.repor_estoque(10)
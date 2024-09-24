# Desenvolver a classe Conta_Agua, com os atributos titular, consumo_m3, e
# tarifa_por_m3;
# Crie o método cadastrar_conta, onde é feita a recepção dos valores dos
# atributos, passados do programa principal;
# Crie o método calcular_valor_conta, onde será calculado o valor da conta, e
# depois impresso na tela, juntamente com o nome do titular da conta;

class Conta_Agua:
        def cadastrar_conta(self):
            self.titular = str(input("Digite o titular da conta: "))
            self.consumo = float(input("Digite o valor do consumo: "))
            self.tarifa = float(input("Digite o valor da tarifa: "))
        
        def calcular_valor_conta(self):
              valor = self.consumo + self.tarifa
              print("O valor do titular ", self.titular, " é: ", valor)

conta1 = Conta_Agua()
conta1.cadastrar_conta()
conta1.calcular_valor_conta()

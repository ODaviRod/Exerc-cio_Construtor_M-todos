class Conta_Agua:
    def __init__(self, titular, consumo, tarifa):
        self.titular = titular
        self.consumo = consumo 
        self.tarifa = tarifa 

    def calcular_valor_conta(self):
        valor = self.consumo * self.tarifa
        print("Titular: ", self.titular)
        print("Conta de água: R$", valor)

conta1 = Conta_Agua("Carlos", 30, 2.5)
conta2 = Conta_Agua("Mariana", 45, 2.5)
conta1.calcular_valor_conta()
conta2.calcular_valor_conta()


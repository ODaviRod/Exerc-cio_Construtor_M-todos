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
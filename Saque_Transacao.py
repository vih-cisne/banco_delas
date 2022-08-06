
from Transacao import Transacao

class Saque_Transacao(Transacao):
    def __init__(self, valor, saldo):
        super().__init__(valor, saldo)
        self.tipo = 'saque' 

    def print_info(self):
        print(f'Saque realizado com sucesso! Você acabou de sacar {self.valor}, seu saldo agora é de {self.saldo}')
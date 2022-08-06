
from Transacao import Transacao

class Deposito_Transacao(Transacao):
    def __init__(self, valor, saldo):
        super().__init__(valor, saldo)
        self.tipo = 'depósito'
        

    def print_info(self):
        print(f'Depósito realizado com sucesso! Você acabou de depositar {self.valor}, seu saldo agora é de {self.saldo}')
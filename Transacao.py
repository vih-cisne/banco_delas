
import datetime 

class Transacao:
    def __init__(self, valor, saldo):
        self.valor = float(valor)  
        self.date = datetime.date.today()
        self.saldo = saldo
        self.info = self.print_info()

    def print_info(self):
        print('Transação realizada com sucesso!')   

    def __str__(self):
        return f'Tipo de transação {self.tipo} - Data {self.date} '
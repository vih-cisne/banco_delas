
import functools

from Deposito_Transacao import Deposito_Transacao
from Saque_Transacao import Saque_Transacao

class Conta_Corrente:
    def __init__(self, titulares):
        self.titulares = titulares
        self.saldo = 0
        self.historico = []

    def saque(self, valor):
        valor = float(valor)
        cheque_especial_media = functools.reduce(lambda acc, t: acc+t.cheque_especial if t.cheque_especial != None else acc, self.titulares,0)
        if(cheque_especial_media != 0):
            cheque_especial_media = cheque_especial_media/len(self.titulares) 
        self.cheque_especial = cheque_especial_media
        if(self.saldo + self.cheque_especial >= valor):
            self.saldo -= valor
            self.historico.append(Saque_Transacao(valor, self.saldo))
            return 
        else:
            print('Desculpa, saldo insuficiente')

    def deposito(self, valor):
        valor = float(valor)
        self.saldo += valor
        self.historico.append(Deposito_Transacao(valor, self.saldo))
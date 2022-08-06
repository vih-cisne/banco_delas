
class Cliente:
    def __init__(self, nome, telefone, renda_mensal, genero):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = float(renda_mensal)
        self.genero = genero
        self.cheque_especial = (None,self.renda_mensal)[self.genero == 'f']
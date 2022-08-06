# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.

from Cliente import Cliente
from Conta_Corrente import Conta_Corrente



# Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo.

                    

def app_banco():
    iniciar = input('Olá, bem vindo ao banco delas, deseja ser nosso cliente? \nDigite 1 se deseja continuar: ')
    if(iniciar == '1'):
        nome = input('Vamos lá! \nDigite seu nome, por favor: ')
        telefone = input('Agora, seu número de telefone: ')
        renda_mensal = input('Qual a sua renda mensal? Digita aqui: ')
        genero = input('E por último, seu gênero, digite f para feminino e m para masculino: ')
        if(genero == 'm' or genero == 'f'):
            print('Um instante...')
            novo_cliente = Cliente(nome, telefone, renda_mensal, genero)
            message = ''
            if(novo_cliente.genero == 'f'):
                message = f' Ah, e como você é mulher, temos um presentinho, acabamos de te dar um cheque especial de R${novo_cliente.cheque_especial:0.2f}.'
            criar_conta_corrente = input(f'Conta criada!{message} Que tal criar uma conta corrente para você? \nDigite 1 se deseja continuar: ')
            if(criar_conta_corrente == '1'):
                print('Ok, estamos criando sua conta...')
                conta_corrente = Conta_Corrente([novo_cliente])
                operacao = input('Yeahh, conta corrente criada! Agora você pode fazer depósitos e saques\nDigite 1 se deseja fazer um depósito\nDigite 2 se deseja fazer um saque\nDigite 0 para sair\nSua opção: ')
                while operacao != '0':
                    if(operacao == '1'):
                        valor = input('Digite o valor do depósito: ')
                        conta_corrente.deposito(valor)

                    elif(operacao == '2'):
                        valor = input('Digite o valor do saque: ')
                        conta_corrente.saque(valor)
                    else:
                        print('Desculpa, comando não reconhecido')
                    operacao = input('Desejar fazer outra operação? \nDigite 1 se deseja fazer um depósito\nDigite 2 se deseja fazer um saque\nDigite 0 para sair\nSua opção: ')
                if(operacao == '0'):
                    print('Até logo!')
        else:
            print('Desculpa, comando não reconhecido')                
    else:
        print('Desculpa, comando não reconhecido')

app_banco()        





 

# 1. Cada conta corrente pode ter um ou mais clientes como titular.

# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.

# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.

#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 

#    fizer um depósito, aumentaremos o saldo.

# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda

#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até

#    -renda_mensal.

# 5. Clientes homens por enquanto não têm direito a cheque especial.
 

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo".

# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".
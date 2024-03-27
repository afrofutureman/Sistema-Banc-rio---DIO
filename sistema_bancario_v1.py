# O sistema deve permitir três saques diários com o valor máximo de R$500.00.
# Não se deve permitir saques de valores que o cliente não tem.
# O Sistema deve emitir uma mensagem de falta de saldo caso o usuário tente acessar a funcionalidade sem dinheiro.
# Todos os saques devem ser exibidos em uma variável de extrato

#Operação extrato deve constar todos os depósitos e saques
#no fim da listagem deve exibir o saldo atual da conta

import time

total_na_conta = 0
valor_deposito = 0

def deposito():
    valor_deposito = float(input("Quanto você está depositando?\n"))
    print("Um momento. Contando as cédulas...\n")
    time.sleep(5)
    print(f"Você depositou {valor_deposito:.2f}")
    total_na_conta = valor_deposito + total_na_conta

    return total_na_conta
print(total_na_conta)

while True:
    escolha = input("Digite [d] parara DEPÓSITO\nDigite [s] para SAQUE\nDigite [e] para EXTRATO\nDigite [0] para SAIR\n")

    if escolha == 'd':
        print("Depósito: ")
        time.sleep(3)
        deposito()

    elif escolha == 's':
        print("Saque: ")
    elif escolha == 'e':
        print("Extrato: ")
    elif escolha == 0:
        break
    else:
        print("Opção inválida. Por favor insira uma opção correta")




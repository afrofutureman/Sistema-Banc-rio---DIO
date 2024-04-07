#adicionar a função de cadastro de cliente- armazenar usuários em uma lista (nome, data de nascimento, cpf, endereço(logradouro, numero - bairro - cidade/sigla estado))
#casdastrar conta bancária: agência, numero da conta e usuário.  agência é fixo numero 0001
#função de saque deve receber argumentos apenas por nome (keyword only)
#função depósido (positional only), só posições, sem valor igual a tal
#função de depósito deve receber os dois tipos
total_na_conta = 0
saques_realizados = 0
SAQUES_POR_DIA = 3
historico = []

def deposito():
    global historico
    global total_na_conta
    valor_deposito = float(input("Quanto você está depositando?\n"))

    if valor_deposito > 0:
        print("Depósito realizado com sucesso!\n")
    else:
      print("Valor inválido!\n")
      valor_deposito = float(input("Quanto você está depositando?\n"))
    historico.append("Depósito +R$" + format(valor_deposito, ".2f"))
    total_na_conta += valor_deposito
    print(f"Você depositou R${valor_deposito:.2f}")

    return total_na_conta

def saque():
  global historico
  global SAQUES_POR_DIA
  global total_na_conta
  global saques_realizados 
  saque = float(input("Digite quanto deseja sacar: "))
  
  if saque > total_na_conta or saque > 500.00:
    print("Operação não pode ser realizada: Verifique seu saldo e/ou limite por saque.")
  elif saque <= 0:
    print("Valor inválido!")
    saque = float(input("Digite quanto deseja sacar: "))
  elif saques_realizados >= SAQUES_POR_DIA:
     print("Limite de saques diários atingido!")
  else:
    print(f"Você acaba de sacar R${saque:.2f}")
    total_na_conta -= saque
    historico.append("Saque -R$" + format(saque, ".2f"))
    saques_realizados += 1
  
  return total_na_conta, saques_realizados

def extrato():
  print("=======EXTRATO======")
  for i in range(len(historico)):
      print("--------------------")
      print(historico[i])
  print("--------------------")
  print(f"Saldo: R${total_na_conta:.2f}")
  print("====================")
    
  
while True:
    escolha = input("Digite [d] para DEPÓSITO\nDigite [s] para SAQUE\nDigite [e] para EXTRATO\nDigite [0] para SAIR\n")

    if escolha == 'd':
        print("Depósito: ")
        deposito()

    elif escolha == 's':
        print("Saque: ")
        saque()
      
    elif escolha == 'e':
        print("Extrato: ")
        extrato()
    elif escolha == 0:
        break
    else:
        print("Opção inválida. Por favor insira uma opção correta")
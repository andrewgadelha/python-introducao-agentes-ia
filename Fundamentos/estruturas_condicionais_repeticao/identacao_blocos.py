saldo = 500

def sacar(valor):
   

    if saldo >= valor:
        print("Saque realizado com sucesso!")
        print("Retire seu dinheiro na boca do caixa.")
    else:
        print("Saldo insuficiente para realizar o saque.")
        
    print("Obrigado por utilizar nosso caixa eletrônico.")

def depositar(valor):
    

    if valor > 0:
        print("Depósito realizado com sucesso!")
        print("Seu novo saldo é: R$", saldo + valor)
    else:
        print("Valor de depósito inválido.")

    print("Obrigado por utilizar nosso caixa eletrônico.")


sacar(1000)
depositar(200)
conta_normal = False
conta_universitaria = False


saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
        print("Retire seu dinheiro na boca do caixa.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
        print("Retire seu dinheiro na boca do caixa.")
    else:
        print("Não foi possível realizar o saque.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
        print("Retire seu dinheiro na boca do caixa.")
    else:
        print("Saldo insuficiente para realizar o saque.")
else:
    print("Tipo de conta inválido.")
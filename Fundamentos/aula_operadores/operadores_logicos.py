# AND - Retorna True se ambas as condições forem True
# OR - Retorna True se uma das condições for True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao_2)


conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

expressao_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao_3)
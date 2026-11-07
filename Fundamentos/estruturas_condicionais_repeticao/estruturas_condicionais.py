MAIORIDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

if idade >= MAIORIDADE:
    print("Pode tirar a carteira de motorista.")
else:
    print("Não pode tirar a carteira de motorista.")



if idade >= MAIORIDADE:
    print("Pode tirar a carteira de motorista.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode dirigir.")
else:
    print("Não pode tirar a carteira de motorista.")

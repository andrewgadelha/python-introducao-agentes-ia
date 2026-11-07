nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


print("Olá, ", nome, "você tem", idade, "anos.")
print("teste", end=" ")
print(nome, idade, end="...\n")
print(nome, idade, sep="##")
print(nome, idade, sep="##", end="...\n")
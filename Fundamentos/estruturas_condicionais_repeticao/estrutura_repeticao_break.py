while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        print("Número 10 encontrado, saindo do loop.")
        break   

    print(numero)

for numero in range(100):

    if numero %2 == 0:
        continue

    print(numero, end=" ")
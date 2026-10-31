texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
       print(letra, end=" ")
else:
    print( )
    print("Fim do programa.")

#Exemplo utilizando for com a função built-in range() para gerar uma sequência de números de 0 a 50, com passo de 5
for numero in range(0, 51, 5):
    print(numero, end=" ")
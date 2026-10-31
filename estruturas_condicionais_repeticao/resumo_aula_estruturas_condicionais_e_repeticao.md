# Resumo da aula: estruturas condicionais e de repetição em Python

Nesta aula, aprendemos os conceitos fundamentais de decisões e repetições em Python, que são essenciais para controlar o fluxo de um programa.

## 1) Estruturas condicionais

As condicionais permitem executar blocos de código apenas quando uma condição for verdadeira.

### `if`, `elif` e `else`

- `if`: executa um bloco quando a condição for verdadeira.
- `elif`: adiciona outra condição caso a anterior seja falsa.
- `else`: executa quando nenhuma condição anterior for atendida.

Exemplo:

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode tirar a carteira de motorista.")
elif idade >= 17:
    print("Pode fazer aulas teóricas, mas não pode dirigir.")
else:
    print("Não pode tirar a carteira de motorista.")
```

### Condição aninhada

É possível colocar um `if` dentro de outro `if`, criando condições mais específicas.

### Condição ternária

A forma compacta de decisão em uma linha:

```python
idade = 20
resultado = "Maior de idade" if idade >= 18 else "Menor de idade"
print(resultado)
```

## 2) Indentação e blocos

Em Python, a indentação define o bloco do código. Sem a indentação correta, o programa pode falhar ou ter lógica incorreta.

Isso é essencial em:
- condicionais
- laços de repetição
- funções
- estruturas de código em geral

## 3) Estruturas de repetição

### `while`

O `while` repete um bloco enquanto a condição for verdadeira.

Exemplo:

```python
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Saindo do sistema...")
```

### `for`

O `for` percorre itens de uma sequência, como uma string, lista ou intervalo gerado por `range()`.

Exemplo:

```python
for numero in range(0, 51, 5):
    print(numero, end=" ")
```

## 4) Comandos `break` e `continue`

### `break`

Interrompe imediatamente o laço em que está sendo executado.

Exemplo:

```python
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        print("Número 10 encontrado, saindo do loop.")
        break

    print(numero)
```

### `continue`

Pula a execução do restante do bloco atual e vai para a próxima iteração do laço.

Exemplo:

```python
for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")
```

## 5) Conclusão

A aula mostrou que Python permite controlar a execução do código por meio de:

- decisões (`if`, `elif`, `else`)
- repetições (`while`, `for`)
- interrupções de fluxo (`break`, `continue`)
- organização visual por indentação

Esses conceitos são a base para construir programas mais dinâmicos, interativos e eficientes.

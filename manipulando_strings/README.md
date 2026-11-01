# Manipulando Strings em Python

Esta aula revisa os principais conceitos de manipulação de strings em Python, com exemplos práticos e exercícios simples.

## 1. Transformação de texto

### `upper()`
Converte todas as letras para maiúsculas.

```python
nome = "AnDreW"
print(nome.upper())  # ANDREW
```

### `lower()`
Converte todas as letras para minúsculas.

```python
print(nome.lower())  # andrew
```

### `title()`
Deixa a primeira letra de cada palavra em maiúscula.

```python
print(nome.title())  # Andrew
```

Esses métodos ajudam a padronizar textos antes de comparações e exibições.

---

## 2. Remoção de espaços em branco

Em Python, espaços no início e no fim de uma string podem atrapalhar processamento e formatação.

### `strip()`
Remove espaços do início e do fim.

```python
texto = "   Python é uma linguagem de programação incrível!   "
print(texto.strip() + "|")
```

### `lstrip()`
Remove espaços à esquerda.

```python
print(texto.lstrip() + "|")
```

### `rstrip()`
Remove espaços à direita.

```python
print(texto.rstrip() + "|")
```

Esses métodos são muito úteis para limpar entradas de usuário e arquivos.

---

## 3. Centralização e alinhamento

### `center()`
Centraliza o texto dentro de um espaço informado.

```python
menu = "Python"
print(menu.center(14))
print(menu.center(14, "#"))
```

Resultado: o texto é ajustado para ficar centralizado em um comprimento definido.

---

## 4. Iteração sobre string

Podemos percorrer cada caractere da string com um loop.

```python
for letra in menu:
    print(letra, end="-")
print()
```

Isso permite acessar cada item da string individualmente, como se fosse uma sequência.

---

## 5. Junção de caracteres

### `join()`
Cria uma string juntando os caracteres de outra string com um separador.

```python
print("-".join(menu))
```

Exemplo:

```python
"P-y-t-h-o-n"
```

`join()` é muito útil para formatar listas e textos.

---

## 6. Fatiamento de strings (slicing)

Strings em Python podem ser acessadas por índice.

```python
nome = "Jean Elaine Grey"

print(nome[0])      # J
print(nome[-1])     # y
print(nome[:5])     # Jean 
print(nome[5:])     # Elaine Grey
print(nome[5:12])   # Elaine
print(nome[5:12:3])
print(nome[:])
print(nome[::-1])
```

### Conceitos importantes:
- `nome[0]`: primeiro caractere
- `nome[-1]`: último caractere
- `nome[:5]`: do início até a posição 4
- `nome[5:]`: da posição 5 até o fim
- `nome[5:12]`: intervalo
- `nome[5:12:3]`: intervalo com passo 3
- `nome[::-1]`: inverte a string

O slicing é uma das operações mais úteis em Python.

---

## 7. Formatação de strings

### `%`
Uma das formas mais antigas de formatar texto.

```python
nome = "Andrew"
idade = 26

print("Nome: %s Idade: %d" % (nome, idade))
```

### `.format()`
Melhor legibilidade e mais flexível.

```python
dados = {"nome": "Andrew", "idade": 26}

print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1}".format(idade, nome))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))
```

### f-strings
A forma mais moderna e prática de formatar textos.

```python
saldo = 45.435

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: 10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: .2f}")
```

As f-strings deixam o código mais limpo e fácil de ler.

---

## 8. Strings multi linha

Em Python, é possível criar textos em várias linhas usando aspas triplas.

```python
nome = "Andrew"

mensagem = f'''
    Olá meu nome é {nome},
        Eu estou aprendendo Python.
Essa mensagem tem diferentes recuos.
'''
print(mensagem)
```

Também pode ser usado para criar menus e textos formatados:

```python
print('''
    ------------ MENU ------------

    1 - Depositar
    2 - Sacar
    0 - Sair

    ------------------------------
     Obrigado por usar esse sistema!!!
''')
```

Isso é muito útil para exibir mensagens, relatórios e interfaces simples em terminal.

---

## 9. Resumo dos principais conceitos

Nesta aula, vimos:

- manipulação de letras (`upper`, `lower`, `title`)
- limpeza de espaços (`strip`, `lstrip`, `rstrip`)
- centralização (`center`)
- leitura de caracteres com loop
- concatenação e separação (`join`)
- fatiamento de strings (`slicing`)
- formatação com `%`, `.format()` e f-strings
- criação de textos em múltiplas linhas

Esses conhecimentos são fundamentais para trabalhar com entradas, saídas e textos em qualquer aplicação Python.

---

## 10. Exemplo final

```python
nome = "Andrew"
idade = 26
print(f"Olá, {nome}! Você tem {idade} anos.")
```

Resultado:

```python
Olá, Andrew! Você tem 26 anos.
```

Esse é um exemplo simples do poder de manipulação e apresentação de strings em Python.

---

## Arquivos da aula

- `string_1.py` — uppercase, lowercase, title e ajustes de espaçamento
- `string_2.py` — formatação de textos com `%`, `.format()` e f-string
- `string_3.py` — slicing e inversão de string
- `string_4.py` — strings multilinha e mensagens formatadas



# Python: do primeiro `print` às estruturas de dados

> **Meu caderno de estudos** no bootcamp **Bradesco — Agentes de IA: do Zero à Prática**, da [DIO](https://www.dio.me/).

Este repositório reúne os scripts e exercícios apresentados e praticados nas aulas. Começando pelo `Hello World!`, o conteúdo passa por variáveis, operadores, decisões, repetições, manipulação de texto e listas. Os códigos são exemplos trabalhados durante o bootcamp; este README é meu registro dos assuntos estudados e do que vou aprendendo ao acompanhar as aulas.

Tenho curiosidade sobre como esses fundamentos se conectam a programas maiores e, mais adiante, a automações e agentes de IA. Por enquanto, estou construindo essa base um exemplo de cada vez.

## Minha trilha até aqui

Os assuntos aparecem nesta ordem no meu percurso:

1. **Primeiros conceitos:** variáveis, tipos, entrada e saída de dados.
2. **Operadores:** cálculos, comparações e lógica booleana.
3. **Fluxo do programa:** condições, laços e interrupções.
4. **Strings:** operações e métodos para trabalhar com texto.
5. **Listas:** formas de agrupar e acessar informações.

São scripts pequenos e independentes.

## Mapa do repositório

```text
.
├── Fundamentos/
│   ├── aula01/                              # Primeiros conceitos de Python
│   ├── aula_operadores/                     # Operadores da linguagem
│   ├── estruturas_condicionais_repeticao/   # Decisões e laços
│   ├── manipulando_strings/                 # Operações com texto
│   └── README.md                            # Apresentação dos fundamentos
├── Estrutura_Dados/
│   └── 01_Listas/                           # Primeiros passos com listas
└── README.md                                # Você está aqui
```

### 1. Fundamentos da linguagem

Na pasta [Fundamentos](./Fundamentos/), estão os exemplos vistos nas aulas sobre os primeiros conceitos da linguagem, cálculos e controle do comportamento de um programa.

#### Aula 01 — primeiros conceitos

Em [Fundamentos/aula01](./Fundamentos/aula01/), acompanhei exemplos introdutórios sobre execução de scripts, exibição de informações no terminal e uso de valores.

| Arquivo | Conteúdo visto em aula |
| --- | --- |
| [primeiro_programa.py](./Fundamentos/aula01/primeiro_programa.py) | Exibição de uma mensagem com `print`. |
| [print_input.py](./Fundamentos/aula01/print_input.py) | Exibição de informações e entrada de dados pelo terminal. |
| [tipos_de_dados.py](./Fundamentos/aula01/tipos_de_dados.py) | Diferentes tipos para representar informações. |
| [variaveis_constantes.py](./Fundamentos/aula01/variaveis_constantes.py) | Nomes para guardar valores e deixar o código mais compreensível. |
| [conversao_tipos.py](./Fundamentos/aula01/conversao_tipos.py) | Conversões entre tipos de dados. |

#### Aula de operadores

Em [Fundamentos/aula_operadores](./Fundamentos/aula_operadores/), acompanhei exemplos de como os valores se relacionam: alguns operadores fazem cálculos, outros comparam valores ou ajudam a compor condições. O [resumo da aula](./Fundamentos/aula_operadores/README.md) reúne os conceitos estudados.

| Arquivo | Tema |
| --- | --- |
| [operadores_aritimeticos.py](./Fundamentos/aula_operadores/operadores_aritimeticos.py) | Operações matemáticas, como soma, divisão e potência. |
| [operadores_atribuicao.py](./Fundamentos/aula_operadores/operadores_atribuicao.py) | Atribuição e atualização de valores. |
| [operadores_comparacao.py](./Fundamentos/aula_operadores/operadores_comparacao.py) | Comparações que resultam em `True` ou `False`. |
| [operadores_logicos.py](./Fundamentos/aula_operadores/operadores_logicos.py) | Combinação e negação de condições com `and`, `or` e `not`. |
| [operadores_associacao.py](./Fundamentos/aula_operadores/operadores_associacao.py) | Verificação de pertencimento com `in` e `not in`. |
| [operadores_identidade.py](./Fundamentos/aula_operadores/operadores_identidade.py) | Identidade de objetos com `is` e `is not`. |

#### Estruturas condicionais e de repetição

Aqui estudei como um programa escolhe caminhos e repete ações. Em [Fundamentos/estruturas_condicionais_repeticao](./Fundamentos/estruturas_condicionais_repeticao/), estão os exemplos vistos em aula com `if`, `elif`, `else`, `for`, `while` e controle de laços. O [resumo da aula](./Fundamentos/estruturas_condicionais_repeticao/resumo_aula_estruturas_condicionais_e_repeticao.md) reúne anotações sobre esses conceitos.

| Arquivo | Conteúdo visto em aula |
| --- | --- |
| [estruturas_condicionais.py](./Fundamentos/estruturas_condicionais_repeticao/estruturas_condicionais.py) | Decisões usando condicionais. |
| [estrutura_condicional_aninhada.py](./Fundamentos/estruturas_condicionais_repeticao/estrutura_condicional_aninhada.py) | Condições dentro de outras condições. |
| [estrutura_condicional_ternaria.py](./Fundamentos/estruturas_condicionais_repeticao/estrutura_condicional_ternaria.py) | Uma forma compacta de escrever uma decisão. |
| [identacao_blocos.py](./Fundamentos/estruturas_condicionais_repeticao/identacao_blocos.py) | O papel da indentação na organização dos blocos. |
| [estrutura_repeticao_for.py](./Fundamentos/estruturas_condicionais_repeticao/estrutura_repeticao_for.py) | Percorrer sequências e intervalos com `for`. |
| [estrutura_repeticao_while.py](./Fundamentos/estruturas_condicionais_repeticao/estrutura_repeticao_while.py) | Repetir ações enquanto uma condição for verdadeira. |
| [estrutura_repeticao_break.py](./Fundamentos/estruturas_condicionais_repeticao/estrutura_repeticao_break.py) | Interromper um laço com `break`. |

#### Manipulando strings

Em [Fundamentos/manipulando_strings](./Fundamentos/manipulando_strings/), os exemplos das aulas mostram maneiras de transformar, formatar e percorrer textos. Entre os assuntos estão tarefas como mudar maiúsculas e minúsculas ou remover espaços usando métodos de Python.

- [string_1.py](./Fundamentos/manipulando_strings/string_1.py)
- [string_2.py](./Fundamentos/manipulando_strings/string_2.py)
- [string_3.py](./Fundamentos/manipulando_strings/string_3.py)
- [string_4.py](./Fundamentos/manipulando_strings/string_4.py)

### 2. Estruturas de dados: listas

Em [Estrutura_Dados/01_Listas](./Estrutura_Dados/01_Listas/), estão os exemplos de aula sobre coleções: como guardar vários valores juntos, acessar itens por posição e organizar dados em sequências e matrizes.

| Arquivo | Conteúdo visto em aula |
| --- | --- |
| [00_declarando_listas.py](./Estrutura_Dados/01_Listas/00_declarando_listas.py) | Diferentes maneiras de criar listas. |
| [01_acesso_direto.py](./Estrutura_Dados/01_Listas/01_acesso_direto.py) | Acessar elementos usando suas posições. |
| [02_indices_negativos.py](./Estrutura_Dados/01_Listas/02_indices_negativos.py) | Usar índices negativos para contar a partir do fim. |
| [03_matriz.py](./Estrutura_Dados/01_Listas/03_matriz.py) | Organizar listas como uma matriz. |
| [04_fatiamento.py](./Estrutura_Dados/01_Listas/04_fatiamento.py) | Selecionar partes de uma sequência. |

## Como estou executando os exemplos

Com Python instalado, executo os scripts a partir da raiz do repositório, informando o caminho do arquivo:

```bash
python Fundamentos/aula01/primeiro_programa.py
```

No Windows, se o comando `python` não estiver disponível, tente:

```powershell
py Fundamentos\aula01\primeiro_programa.py
```

Para executar outro exemplo, troco o caminho pelo arquivo correspondente. Alguns scripts pedem dados pelo terminal; nesses casos, vou respondendo às perguntas que aparecem.

## O que tenho praticado

- **Executar os exemplos:** observar no terminal o resultado de cada trecho.
- **Mudar pequenos detalhes:** alterar entradas, condições e valores para testar minhas hipóteses.
- **Prestar atenção aos fundamentos:** tipos, índices e indentação podem mudar o resultado.
- **Revisar as anotações:** voltar aos resumos quando quero conectar ou relembrar conceitos.

> Este repositório acompanha meus estudos no bootcamp da DIO. Os scripts são exemplos e exercícios trabalhados em aula; este README organiza os temas e registra minha jornada de aprendizado em Python.

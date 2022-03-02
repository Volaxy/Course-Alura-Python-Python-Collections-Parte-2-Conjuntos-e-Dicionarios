# Python Collections Parte 2 - Conjuntos e Dicionários

Curso da Alura sobre conjuntos de dicionários e como trabalhar com eles

## Objetivo Final &#x1F3AF;

Representar vários conjuntos e seus métodos

URL do curso -> [Python Collections Parte 2 - Conjuntos e Dicionários](https://cursos.alura.com.br/course/python-collections-conjuntos-e-dicionarios)

![Python Collections Parte 2 - Conjuntos e Dicionários](https://www.alura.com.br/assets/api/share/curso-python-collections-conjuntos-e-dicionarios.png)

## Links Úteis &#x1F517;
*

## Siglas &#x1F5FA;
*

## Atalhos &#x2328;
*

## 01 - Conjuntos &#x1F516;
* O que são Conjuntos.
* Criar conjuntos.
* Utilizar o `|` para juntar conjuntos.
* Utilizar o `&` para juntar apenas números que estão no mesmo conjunto.
* Utilizar o `-` para remover números repetidos que estão no em dois conjuntos.
* O que é ou `(^)` exclusivo.

### 01 - Trabalhando com Conjuntos, os Sets
* `.copy()` cria uma cópia de uma lista.
* `set` para criar um conjunto.
    * Um conjunto é representado com os valores entre `{x, y, ...}`.
* A união de 2 conjuntos usando `|`.

### 02 - Mais Operações de Conjuntos
* Usar o `&` para representar a interseção de 2 conjuntos.
* Usar o `-` como exclusão entre 2 conjuntos.

## 02 - Operações &#x1F516;
* Modificar o conjunto em tempo real.
* Congelar o conjunto com o `frozenset`.
* Tirar a duplicidade de uma String.
* Adicionar elementos no conjunto.

### 01 - Outro tipo de Conjunto e Conjuntos de outros Tipos
* Adicionar novos elementos com `add()`.
* Evitar que o conjunto seja alterado com `frozenset()`.

## 03 - Dicionários &#x1F516;
* O que é um dicionário.
* Verificar se o elemento está dentro do dicionário.
* Utilizar o `get` para verificação.
* Criar um dicionário a partir do `dict`.
* Adicionar um elemento no dicionário.
* Remover um elemento do dicionário.
* Mostrar os elementos dentro do dicionário.
* Usar a função `keys` para pegar as chaves.
* Usar a função `values` para pegar os valores.
* Percorrer linha a linha com a função `items`.

### 01 - Dicionários
* Um **Dicionário** no **Python** é um conjunto *chave* e *valor*.
* `VARIABLE = { "KEY" : VALUE, ...}` ou `VARIABLE = dict(KEY = ?, VALUE = ?)` para criar um **Dicionário**.
* `DICTIONARY[KEY]` ou `DICTIONARY.get(KEY)` para acessar o valor de uma chave.

### 02 - Mais Operações de Dicionários
* `del DICTIONARY[KEY]` para remover um elemento do **Dicionário**.
* `KEY in DICTIONARY` para verificar se existe uma chave dentro do **Dicionário**.
* `DICTIONARY.keys()` para acessar as *chaves* do **Dicionário**.
* `DICTIONARY.values()` para acessar as *valores* do **Dicionário**.
* `DICTIONARY.items()` para acessar os conjuntos *chave* e *valor* do **Dicionário**.

## 04 - Variações de Dicionários &#x1F516;
* Contar quantas vezes aparece uma palavra.
* Utilizar o `default dict`.
* Utilizar o `Counter` para contar valores.

### 01 - Default dict
* Construir um dicionário com valores padrão com `dafultdict()`.

### 02 - Counter
* O `Counter()` conta cada elemento da lista e cria um dicionário com os valores.
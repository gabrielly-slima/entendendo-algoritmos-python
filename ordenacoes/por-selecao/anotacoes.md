# Ordenação por seleção
A ordenação por seleção é um algoritmo que organiza uma base de dados em estruturas que oferecem acesso direto aos elementos, como arrays ou listas no Python. Para que a ordenação ocorra, é necessário definir um critério de ordenação, que pode ser crescente, decrescente ou baseado em algum atributo específico dos dados (ex: nível de prioridade, incidência...). O funcionamento do algoritmo ocorre através de comparações sucessivas, onde, a cada ciclo, ele procura o menor elemento da parte que falta ordenar e troca com o elemento que está na primeira posição dessa parte, até que toda a estrutura esteja ordenada.

[Vídeo exemplificando](https://youtu.be/0LPul4lZ_po?si=TT_P6Uu2ia0LRFcH)

## Explicação do vídeo

1. Recebe a base de dados (uma lista de elementos)
2. Define o elemento na posição atual (começando pelo índice 0) como o menor encontrado até o momento
3. Conta quantos índices existem na base de dados para saber até onde precisa percorrer
4. Percorre os elementos a partir do índice seguinte (índice atual + 1) e compara cada um com o menor atual
5. Se encontrar um elemento menor, atualiza qual é o menor da rodada (não troca ainda)
6. Ao finalizar a varredura dessa rodada, troca o menor elemento encontrado com o elemento da posição atual
7. Avança para o próximo índice e repete esse processo até o penúltimo índice da lista
8. Ao final, toda a lista estará ordenada

## Complexidade
O algoritmo de ordenação por seleção possui complexidade de tempo **O(n²)** em todos os casos (melhor, médio e pior), pois realiza sempre o mesmo número de comparações, independentemente da ordem dos dados. Isso acontece porque ele percorre toda a base de dados repetidamente para encontrar o menor elemento de cada ciclo.
Em relação à memória, é considerado eficiente, com complexidade de espaço O(1), pois não utiliza estruturas auxiliares — a ordenação ocorre na própria base de dados (in-place).

# Pesquisa Binária
---

## O que é?
A pesquisa binária é um algoritmo. Sua entrada é uma lista ordenada de elementos. Se o elemento que você buscar estiver na lista, a pesquisa binária retorna o índice de sua localização e caso não encontre, a pesquisa binária retorna None.

## Funcionalidade:
Ao contrário da pesquisa simples, a pesquisa binária retorna com eficiência e rapidez a posição do item buscado. Isso porque, na pesquisa simples é analisado um item por vez até encontrar o alvo. Enquanto na pesquisa binária, o tempo de busca é reduzido pois divide-se repetidamente a lista no meio aplicando-se um método de comparação na procura. A pesquisa binária, essa forma tão eficiente de buscar por elementos numa lista funciona da seguinte forma:

1. Começa pelo item que está no meio (retornando o índice de sua posição);
#### Obs: O índice refere-se ao número que identifica a posição de um elemento dentro de uma sequência. O índice começa em 0, e cada elemento subsequente tem o índice incrementado em 1.

2.  Se o item do meio for igual ao que você estiver procurando, retorna o item e sua pesquisa acabou;

3. Se o item do meio for maior que o item que você estiver procurando repete a pesquisa utilizando somente metade da lista, a parte da esquerda;

4. Se o item do meio for menor que o item que você estiver procurando repete a pesquisa utilizando somente metade da lista, a parte da direita;

5. Isso se repete até que encontre a posição do item desejado;

### Exemplo 
Se eu quero encontrar uma palavra num dicionário que possui 120.000 palavras, utilizando a busca simples eu teria que olhar as 120.000 para encontrar a que estou procurando. Já com a pesquisa binária, a cada etapa elimina-se metade das palavras. Dessa maneira:

120K → 60K → 30K → 15K → 7.5K → 3.75K → 1.875K → 938 → 469 → 235 → 118 → 59 → 30 → 15 → 8 → 4 → 2 → 1.

De 120.000 etapas necessárias para localizar a palavra na pesquisa simples, reduz para 17 utilizando a busca binária.

## Lógica da Busca Binária
Analisando o algoritmo de pesquisa binária podemos concluir que a cada busca elimina-se cerca de metade dos itens que estavam sendo considerados. Tendo (n) como a quantidade de numeros na lista, na primeira comparação realizada restariam então n/2 itens, na segunda comparação n/4, na terceira n/8, na quarta n/16 e assim por diante. A tabela a seguir expõe figuramente o exemplo exposto:

Comparações| Nº aproximado que restam
---|---
1| n/2
2| n/4
3| n/8
4| n/16

É possível então, estabelecer um raciocínio lógico para tudo isso pois, quando usamos a busca binária, sempre dividimos a lista pela metade a cada passo. Isso faz com que o número de elementos que ainda precisamos verificar fique cada vez menor, bem rápido.

Se você tem uma lista com n elementos, na primeira comparação você olha o valor do meio.
Se não for o valor que você quer, descarta metade da lista.
Na próxima, descarta mais metade. E assim vai...

A pergunta é:
Quantas vezes você consegue dividir uma lista ao meio até sobrar só 1 elemento?

A resposta está na conta:

**$n / 2^x = 1$**

Ou seja, depois de x divisões por 2, sobra só 1 item.

Agora, vamos isolar o x (que representa o número de comparações feitas):

**$x = log₂(n)$**

Esse "logaritmo na base 2" quer dizer quantas vezes o número n pode ser dividido por 2 até chegar em 1.

Por isso, o número máximo de comparações na busca binária é log₂(n).
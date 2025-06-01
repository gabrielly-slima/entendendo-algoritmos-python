# Ordenação por intercalação ou Mergesort
A ordenação por intercalação é uma forma de estruturar dados dividindo o problema em subproblemas menores que são resolvidos e em seguida, intercalados para a obtenção do resultado final. É baseado na estratégia "Dividir para conquistar"

## Como funciona
1. Divisão:
Inicialmente, o algoritmo divide a lista em sublistas menores contendo apenas um elemento.
2. Conquista:
A partir dos subproblemas de tamanho 1, o algoritmo começa a intercalar as sublistas ordenadas, formando listas maiores cada vez mais ordenadas.
3. Intercalação:
A intercalação é o processo de combinar duas sublistas ordenadas de tamanho 1, em uma única lista ordenada. Isso é feito comparando os elementos de cada vetor e colocando o menor deles na nova lista, até que um dos vetores seja esgotado. 

### Exemplo:
Se quisermos ordenar a lista [8, 3, 1, 7, 0, 10, 2], o Merge Sort faria o seguinte:

Divisão: A lista é dividida em [8, 3, 1, 7] e [0, 10, 2].
Conquista: As metades são divididas novamente até termos listas de tamanho 1: [8], [3], [1], [7], [0], [10], [2].
Intercalação: As listas de tamanho 1 são intercaladas: [3, 8], [1, 7], [0, 2, 10]. Em seguida, as listas intercaladas são combinadas: [1, 3, 7, 8], [0, 2, 10]. Finalmente, a lista completa é intercalada: [0, 1, 2, 3, 7, 8, 10].

## Complexidade
O Merge Sort tem uma complexidade de tempo de O(n log n), o que o torna um algoritmo eficiente para grandes conjuntos de dados. 

### Prós:
Eficiência: Complexidade de tempo O(n log n) em todos os casos (melhor, médio e pior). 
Estabilidade: Mantém a ordem relativa dos elementos iguais. 
Utilizado em ordenação externa: Pode ser usado para ordenar grandes quantidades de dados que não cabem na memória RAM.

### Contras:
Espaço adicional: Requer espaço extra para armazenar as listas intercaladas (O(n)).
Recursivo: A implementação recursiva pode ser menos eficiente em algumas linguagens de programação. 
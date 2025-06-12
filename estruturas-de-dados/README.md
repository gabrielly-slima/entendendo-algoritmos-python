# Estruturas de dados

Em Python, estruturas de dados são formas organizadas de armazenar e manipular dados, que são essenciais para a programação. As principais estruturas de dados integradas no Python incluem listas, tuplas, conjuntos e dicionários.

## Listas
---
### O que são?
- Estruturas ordenadas e permissíveis a mudanças
- Permite elementos repetidos
- Usa [] - colchetes

#### Exemplo 
frutas = ["maçã","banana","abacaxi","morango"]
frutas.append("uva")
print(frutas) #["maçã","banana","abacaxi","morango","uva"]

##### Métodos mais utilizados
- .append() - Serve para adicionar item no fim da lista
- .insert(i, x): insere na posição i.
- .remove(x): remove o primeiro item com valor x.
- .sort(): ordena a lista.

## Tuplas
---
### O que são?
- Estruturas ordenadas e não permissíveis a mudanças
- Usa () - parenteses
- Mais rápidas que listas (ocupam menos memória por não haver modificação de dados)
- Boas para representar pontos fixos

#### Exemplo
coordenadas = (10, 20)
print(coordenadas[0]) #10

## Conjuntos (set)
---
### O que são?
- Coleção não ordenada e não permissível a mudanças
- Não aceita elementos duplicados

#### Exemplo
letras = set("banana")
print(letras)  # {'b', 'a', 'n'}

##### Métodos mais utilizados
- union(): união de conjuntos
- intersection(): interseção
- difference(): diferença

## Dicionários
---
### O que são?
- Coleções ordenadas e permissíveis a mudanças
- Pares chave-valor (key-value) 

#### Exemplo
aluno = {"nome": "Gaby", "idade": 18}
print(aluno["nome"])  # Gaby

##### Métodos mais utilizados
- .keys(): retorna as chaves
- .values(): retorna os valores
- .items(): retorna os pares
- .get("chave"): retorna o valor da chave
"""
DESAFIO - ORDENAÇÃO POR SELEÇÃO
Imagine que você é o dono de uma pastelaria. Hoje vai acontecer o "Concurso dos Sabores de Pastel" e sua missão é organizar a lista dos pastéis mais pedidos para exibir no painel da loja.
Você recebe uma lista desordenada com os nomes dos sabores e a quantidade de pedidos de cada um. Seu desafio é ordenar essa lista do pastel mais pedido até o menos pedido, utilizando a lógica da ordenação por seleção.
"""

pasteis = [["carne","45"],["queijo","26"],["frango","53"],["calabresa","68"],["pizza","31"]]

def pedidos():
    '''
    Retorna o sabor que obteve o maior número de pedidos e seu respectivo valor.

    Esta função percorre a lista 'pasteis', compara a quantidade de pedidos de cada sabor 
    e imprime o sabor mais pedido junto com a quantidade de pedidos.
    '''

    # Inicializa com o primeiro sabor e sua quantidade como os maiores encontrados até o momento
    num_pedidos = (int(pasteis[0][1])) 
    sabor = pasteis[0][0] 

    # Percorre toda a lista para encontrar o maior número de pedidos
    for i in range(len(pasteis)): 
        try:
            if int(pasteis[i][1]) > num_pedidos:
                num_pedidos = int(pasteis[i][1]) # Atualiza o maior número de pedidos
                sabor = pasteis[i][0]  # Atualiza o sabor correspondente
        except ValueError:
            print("Algo deu errado")
    
    # Exibe o sabor com mais pedidos
    print(f"O sabor que teve mais pedidos foi o de {sabor}, com {num_pedidos} pedidos")

def ordenacao():
    '''
    Ordena e retorna a lista de sabores de pastéis com seus respectivos números de pedidos, 
    em ordem crescente (do menos pedido ao mais pedido).

    A função faz uma cópia da lista 'pasteis' e, utilizando uma lógica de ordenação por seleção,
    encontra o sabor com menor número de pedidos a cada ciclo. 
    Esse item é removido da cópia e adicionado na lista 'painel', que representa a lista ordenada.

    Retorna:
    painel (list): Lista de tuplas (sabor, quantidade de pedidos) ordenada do menor para o maior.
    '''
    
    lista_copia = pasteis.copy()
    painel = []
    while lista_copia:
        menor_valor = (int(lista_copia[0][1]))
        indice_menor_valor = 0
        for i in range(len(lista_copia)):
            if menor_valor < (int(lista_copia[i][1])):
                menor_valor = (int(lista_copia[i][1]))
                indice_menor_valor = i
        painel.append(lista_copia.pop(indice_menor_valor))
    for i in painel:
        print(f"Sabor: {i[0]}, Pedidos: {i[1]}")
    return painel

def main(): 
    print("Concurso dos Sabores de Pastel\n Confira o favorito aqui embaixo:\n")
    pedidos()
    print("Lista dos mais pedidos:\n")
    ordenacao()

main()
"""
DESAFIO - ORDENAÇÃO POR SELEÇÃO
Imagine que você é o dono de uma pastelaria. Hoje vai acontecer o "Concurso dos Sabores de Pastel" e sua missão é organizar a lista dos pastéis mais pedidos para exibir no painel da loja.
Você recebe uma lista desordenada com os nomes dos sabores e a quantidade de pedidos de cada um. Seu desafio é ordenar essa lista do pastel mais pedido até o menos pedido, utilizando a lógica da ordenação por seleção.
"""

pasteis = [["carne","45"],["queijo","26"],["frango","53"],["calabresa","18"],["pizza","31"]]

def mais_pedido():
    num_pedidos = (int(pasteis[0][1]))
    for i in range(len(pasteis)):
        try:
            if int(pasteis[i][1]) > num_pedidos:
                num_pedidos = int(pasteis[i][1])
                sabor = pasteis[i][0]
                print(f"O sabor que teve mais pedidos foi o de {sabor}, com {num_pedidos} pedidos")
        except ValueError:
            print("deu bosta")

mais_pedido()
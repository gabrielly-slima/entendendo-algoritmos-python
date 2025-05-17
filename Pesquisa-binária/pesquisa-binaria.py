def pesquisa_binaria (lista,item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        
        meio = (baixo + alto)//2
        valor_meio = lista[meio]
            
        if valor_meio == item:
            return meio
        
        elif valor_meio > item:
            alto = meio - 1
        
        else:
            baixo = meio + 1
        
    return None

def mensagem_de_erro():
    print("Você digitou um caractere inválido!\n")

try: 
    entrada_lista = (input("Digite uma lista de números, separando-os por espaços:")).strip()
    lista_numeros = [int (n) for n in entrada_lista.split()]
except ValueError:
    mensagem_de_erro()

while True: 
    try:   
        numero = int(input('Digite o número que deseja procurar:\n'))
        resultado_posicao = pesquisa_binaria(lista_numeros, numero)

        if resultado_posicao is not None:
            print(f'O número está na posição', (resultado_posicao))
        else:
            print('Digite um número presente na lista\n')
        

    except ValueError:
        mensagem_de_erro()
        continue
    
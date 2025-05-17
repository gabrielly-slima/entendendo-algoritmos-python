minha_lista = [9,11,13,15,17,19,21]

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

while True: 
    try:   
        numero = int(input('Digite o número que deseja procurar:\n'))
        resultado_posicao = pesquisa_binaria(minha_lista, numero)

        if resultado_posicao is not None:
            print(f'O número está na posição', (resultado_posicao))
        else:
            print('Digite um número presente na lista\n')

    except ValueError:
        print("Você digitou um caractere inválido, digite um número!\n")
        continue
    
    
  
        
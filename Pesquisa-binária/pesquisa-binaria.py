def pesquisa_binaria (lista, numero_procurado):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        
        meio = (baixo + alto)//2
        valor_meio = lista[meio]
            
        if valor_meio == numero_procurado:
            return meio
        
        elif valor_meio > numero_procurado:
            alto = meio - 1
        
        else:
            baixo = meio + 1
        
    return None

def mensagem_de_erro():
    print("Você digitou caracteres inválidos!\n")

try: 
    entrada_lista = (input("Digite uma lista de números, separando-os por espaços:")).strip()
    lista_numeros = [int (n) for n in entrada_lista.split()]
except ValueError:
    mensagem_de_erro()

while True: 
    entrada = input("Digite o número que deseja procurar: \n Para sair digite SAIR\n").strip().upper()

    if entrada == "SAIR":
        print("Encerrando sua busca...")
        break
    
    try: 
        numero = int(entrada)
        resultado_posicao = pesquisa_binaria(lista_numeros, numero)

        if resultado_posicao is not None:
            print(f"O número está na posição {resultado_posicao}")
        
        else:
            print("Número não encontrado...Digite um número presente na lista!\n")

        if voltar_para_lista():
            while True:
                try: 
                    entrada_lista = (input("Digite uma nova lista de números, separando-os por espaços:")).strip()
                    lista_numeros = [int (n) for n in entrada_lista.split()]
                    lista_numeros.sort()
                    print(f"Sua nova lista ordenada é: {lista_numeros}")
                    break
                except ValueError:
                    mensagem_de_erro()

    except ValueError:
        mensagem_de_erro()
        continue



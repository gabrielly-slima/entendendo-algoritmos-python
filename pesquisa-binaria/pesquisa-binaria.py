def pesquisa_binaria(lista, numero_procurado): 
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

def voltar_para_lista():
    resposta = input("Digite VOLTAR, se quiser escrever novamente os números da lista, ou aperte ENTER se decidir continuar procurando os números\n").upper().strip() 

    if resposta == "VOLTAR": 
        return True 
    elif resposta != "": 
        print("Entrada inválida! Continuando a busca com a mesma lista...")
        return False 

def menu_inicial():
    while True:
        print("MENU INICIAL:")

        try: 
            entrada_lista = (input("Digite uma lista de números, separando-os por espaços:\n")).strip() 
            lista_numeros = [int (n) for n in entrada_lista.split()] 
            lista_numeros.sort() 
            return lista_numeros
        except ValueError: 
            mensagem_de_erro() 

def buscar_numero(lista_numeros):
    while True:
        entrada = input("Digite o número que deseja procurar: \n Para sair digite SAIR\n").strip().upper()

        if entrada == "SAIR": 
            print("Encerrando sua busca...")
            return
    
        try:
            numero = int(entrada)
            resultado_posicao = pesquisa_binaria(lista_numeros, numero) 

            if resultado_posicao is not None:
                print(f"O número está na posição {resultado_posicao}")
            else:
                print("Número não encontrado...Digite um número presente na lista!\n")
            if voltar_para_lista():
                return "VOLTAR"
        except ValueError:
            mensagem_de_erro()
            continue

def menu_principal():
    while True:
        lista_numeros = menu_inicial()
        print(f"Sua lista ordenada é: {lista_numeros}")
        resultado = buscar_numero(lista_numeros) 

        if resultado == "sair":
            break
        elif resultado == "voltar":
            continue

menu_principal()



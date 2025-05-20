def pesquisa_binaria(lista, numero_procurado): 
    """
    Realiza uma busca binária em uma lista ordenada

    Parâmetros:
    - lista: A lista de ne números ordenados
    - numero_procurado: número que deseja encontrar.

    Retorna o índice do número encontrado, ou None caso não esteja presente
    """

    #estabelece como baixo o item referente ao indice 0 (o que está no extremo esquerdo da lista)
    baixo = 0 

    #estabelece como alto (o item que está no extremo direito da lista) a conta total de numeros da lista - 1, pois o indice inicia em 0.
    alto = len(lista) - 1 

    while baixo <= alto: #enquanto o item baixo for menor ou igual ao item baixo execute isso:
        meio = (baixo + alto)//2 #para achar a posição meio, soma-se o indice baixo mais o indice alto e divide por 2. Utiliza-se 2 operadores (/) para dividir para que o resultado seja inteiro
        valor_meio = lista[meio] #o item do meio é o que esta no indice da posição do meio da lista
            
        if valor_meio == numero_procurado: #se o item do meio for igual ao item procurado:
            return meio #retorna a posição meio
        elif valor_meio > numero_procurado: #se o item do meio for maior que o item procurado:
            alto = meio - 1 #o item alto vira o item que está na posicão meio - 1, porque a contagem de indices inicia em 0 (a pesquisa agora é na parte esquerda da lista)
        else: #se não for
            baixo = meio + 1 #o item baixo vira o item que está na posição meio + 1 (a pesquisa agora é na parte direita da lista)
    return None #caso não seja retorne nada

def mensagem_de_erro():
    """
    Exibe mensagem de erro ao inserir caracteres inválidos
    """
    print("Você digitou caracteres inválidos!\n")

def voltar_para_lista():
    """"
    Verifica se o usuário deseja reescrever a lista ou continuar a busca.
    Retorna:
    True se o usuário digitou 'VOLTAR'
    False caso contrário
    """        

    resposta = input("Digite VOLTAR, se quiser escrever novamente os números da lista, ou aperte ENTER se decidir continuar procurando os números\n").upper().strip() #Se o usuário escolher voltar, qualquer variação de digitação será aceita, pois todas as letras serão convertidas em maiusculas (upper) e serão removidos espaços em branco do inicio ou do fim da string (strip)

    if resposta == "VOLTAR": #se a resposta digitada pelo usuário for igual a voltar:
        return True 
    elif resposta != "": #se a resposta digitada pelo usuário for diferente de "" (que seria o enter, pois é a ausencia de string"
        print("Entrada inválida! Continuando a busca com a mesma lista...")
        return False 

def menu_inicial():
    """
    Solicita ao usuário uma lista de números separados por espaços
    
    Retorna uma lista ordenada de inteiros digitados pelo usuário
    """

    while True:
        print("MENU INICIAL:")
        try: 
            # Lê a entrada do usuário e remove espaços em branco nas extremidades (strip)
            entrada_lista = (input("Digite uma lista de números, separando-os por espaços:\n")).strip() 
            
            # Transforma em inteiro cada item (n) presente na entrada_lista, todos estes tambem são separados por espaços (split)
            lista_numeros = [int (n) for n in entrada_lista.split()] 
            lista_numeros.sort() #ordena os números de lista_numeros
            return lista_numeros
        except ValueError: 
            mensagem_de_erro() #imprime a mensagem de erro definida na função
    
def buscar_numero(lista_numeros):
    """
    Solicita ao usuário o numero para a busca e retorna sua posição
    Apresenta ao usuario a opção de sair a qualquer momento
    """

    while True:
        # Recebe o número que o usuário quer procurar e se ele escolher sair, qualquer variação dessa palavra será aceita porque, todas as letras serão transformadas em maiusculas. Espaços em branco nas extremidades também serão removidos.
        entrada = input("Digite o número que deseja procurar: \n Para sair digite SAIR\n").strip().upper()

        if entrada == "SAIR": # Se o usuário digitar "SAIR", encerra o loop e a função.
            print("Encerrando sua busca...")
            return
    
        try: 
            #tenta converter a entrada para um número inteiro
            numero = int(entrada)

            # Chama a função 'pesquisa_binaria' passando a lista de números ordenada e o número digitado pelo usuário.
            resultado_posicao = pesquisa_binaria(lista_numeros, numero) 

            # Se a função retornou uma posição (índice), informa ao usuário onde o número foi encontrado.
            if resultado_posicao is not None:
                print(f"O número está na posição {resultado_posicao}")

            # Caso a busca binária não tenha encontrado o número, avisa ao usuário que ele não está na lista.
            else:
                print("Número não encontrado...Digite um número presente na lista!\n")

            # Pergunta se o usuário deseja voltar para a lista 
            # Se sim, a função retorna "VOLTAR" 
            if voltar_para_lista():
                return "VOLTAR"

        except ValueError:
            mensagem_de_erro()
            continue

def menu_principal():
    while True:
        # Chama a função que retorna a lista inicial de números ordenados.
        lista_numeros = menu_inicial()

        # Mostra ao usuário a lista ordenada que foi escolhida
        print(f"Sua lista ordenada é: {lista_numeros}")

        # Chama a função para o usuário buscar um número dentro da lista.
        # A função retorna:
        # - "sair" se o usuário escolher encerrar a busca e sair do programa,
        # - "voltar" se o usuário quiser retornar para a lista inicial e tentar novamente,
        # - None ou outro valor se continuar buscando.
        resultado = buscar_numero(lista_numeros) 

        # Se o usuário escolheu sair, o loop é interrompido e o programa finaliza.
        if resultado == "sair":
            break

        # Se o usuário escolheu voltar, o loop reinicia, mostrando novamente o menu inicial.
        elif resultado == "voltar":
            continue

menu_principal()



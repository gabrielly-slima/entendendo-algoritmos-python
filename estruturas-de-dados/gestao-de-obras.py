#Funcionalidades:
# Selecionar/Criar obra do dia (nome do lugar).
# Cadastrar funcionários presentes no dia, com valor da diária. 
# Cadastrar gastos diversos, como materiais ou transporte (valor + descrição).
# Exibir relatório com:
# Total gasto com funcionários,
# Total de outros gastos,
# Total geral.
# Permitir cadastro diario
# Acesso a todos os gastos cadastrados ate o momento
# Organização sugerida:
# Usar classes: Obra, Funcionario, Gasto.
# Armazenar dados do dia numa lista ou dicionário.
# No final, usar print() para o resumo dos custos.
import re
import hashlib

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Obra:
    def __init__(self):
        self.lugar = []
        self.dia = []
    
    #def adicionar_obra(self):


class Sistema:
    def __init__(self):
        self.usuarios = []
        self.obras = []
        self.gastos = []
    
    def sign_in(self,nome,email,senha):
        cadastro = Usuario(nome,email,senha)
        self.usuarios.append(cadastro)



def main():
    print("GESTÃO OBRAS - BFX\n")
    print("LOG-IN")
    nome = input("Digite seu nome:")

    while True:
        email = input("Digite seu e-mail:")
       
        #.+	Pelo menos um caractere (qualquer) antes do @ | @	O caractere "@" obrigatório | .+	Pelo menos um caractere depois do @ | \.com	Literalmente ".com" (\. escapa o ponto) | $	Fim da string — ou seja, o .com tem que estar no final
        validacao = re.search(r".+@.+\.com$",email) 
        if validacao:
            senha = input("Digite sua senha:")
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()
            sistema = Sistema()
            sistema.sign_in(nome,email,senha_hash)
            print(f"{nome}, bem-vinda a GESTÃO OBRAS - BFX")
            try:
                menu_principal = int(input("MENU PRINCIPAL\n1. Adicionar obra\n2.Ver Relatórios\n3. Consultar gastos"))
                if menu_principal == 1:
                    obra = Obra(lugar,dia)
                    sistema.obras.append(obra)
            except ValueError:
                print("bosta")
        else:
            print("E-mail inválido. Tente novamente")  

            
            

main()
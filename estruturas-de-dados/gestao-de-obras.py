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

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def sucesso(self):
        print(f"{self.nome}, bem-vinda a GESTÃO OBRAS - BFX")
    


class Obra:
    def __init__(self,lugar,dia):
        self.lugar = lugar
        self.dia = dia  
    


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
            criar_usuario = Usuario(nome,email,senha)
            criar_usuario.sucesso()
            return criar_usuario
            
        else:
            print("E-mail inválido. Tente novamente")  

            
            

main()
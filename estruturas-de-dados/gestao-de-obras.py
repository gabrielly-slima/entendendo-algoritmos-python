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
import datetime

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Obra:
    def __init__(self,lugar,dia):
        self.lugar = lugar
        self.dia = dia
    
    #def adicionar_obra(self):


class Sistema:
    def __init__(self):
        self.usuarios = []
        self.obras = []
        self.gastos = []
    
    def menu_de_operacoes(self):
        print("menu de operações")
    
    def sign_in(self,nome,email,senha):
        cadastro = Usuario(nome,email,senha)
        self.usuarios.append(cadastro)

    def log_in(self,email,senha_hash):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == senha_hash:
                return usuario  # Login bem-sucedido
            else:
                print("Senha incorreta.")
                return None
        return None  # E-mail não encontrado


       

    def menu_inicial(self):
        print("GESTÃO OBRAS - BFX\n")
        while True:
            email = input("Digite seu e-mail: ").strip()
            validacao = re.search(r".+@.+\.com$",email) 
            if validacao:
                senha = input("Digite sua senha: ").strip()
                senha_hash = hashlib.sha256(senha.encode()).hexdigest()
            else:
                print("E-mail inválido, tente novamente!")
                continue

            usuario = self.log_in(email, senha_hash)
            if usuario:
                print(f"Bem-vindo(a) de volta, {usuario.nome}!")
                self.menu_de_operacoes()
                return

            else:
                print("E-mail não cadastrado!")
                opcao = input("Deseja se cadastrar? (SIM/NÃO): ").upper().strip()
                if opcao == "SIM":
                    nome = input("Digite seu nome: ").strip()
                    
                    cadastro_feito = self.sign_in(nome, email, senha_hash)
                    if cadastro_feito:
                        print(f"Usuário cadastrado com sucesso. Bem-vindo(a), {nome}!")
                        self.menu_de_operacoes()  # Aqui segue para outro menu
                        return
                    else:
                        print("E-mail inválido, tente novamente!")
                    continue
                
                elif opcao == "NÃO":
                    print("Encerrando o sistema...")
                    break
                else:
                    print("Opção inválida, tente novamente.")
                    continue


sistema = Sistema()
sistema.menu_inicial()
    
    

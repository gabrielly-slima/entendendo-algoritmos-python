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
        print("pegando")
    
    def sign_in(self,nome,email,senha):
        cadastro = Usuario(nome,email,senha)
        self.usuarios.append(cadastro)

    
    
    def log_in(self):
        while True:
            email = input("Digite seu e-mail: ").strip()
            senha = input("Digite sua senha: ").strip()
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()


            for usuario in self.usuarios:
                if usuario.email == email and usuario.senha == senha_hash:
                    print(f"Bem-vindo(a) de volta a GESTÃO OBRAS - BFX, {usuario.nome}!")
                    self.menu_de_operacoes(usuario)
                    return  # Sai da função log_in, login bem-sucedido

                elif usuario.email == email and usuario.senha != senha_hash:
                    print("Senha incorreta. Tente novamente.")
                    continue

                else:
                    cadastrar = input("E-mail não cadastrado. Deseja se cadastrar? (SIM ou NÃO): ").upper().strip()
                    if cadastrar == "SIM":
                    self.sign_in()
                    
                    elif cadastrar == "NÃO":
                        print("Encerrando sistema...")
                        break
            
def main():
    try:
        sistema = Sistema()
        sistema.log_in()
    except ValueError:
        print("ruik")
    
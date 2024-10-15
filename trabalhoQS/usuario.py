
class Usuario:
    def __init__(self, nome: str, senha: str, idade: str, saldo: int = 0, salario: int = 0, ativo: bool = True) -> None:
        self.nome = nome
        self.senha = senha
        self.idade = idade
        self.saldo = saldo
        self.salario = salario
        self.ativo = ativo
    

    def get_salario_anual(self):
        return self.salario * 12


ADMIN_USER = Usuario('admin', 'admin123', 30, 1000, 1500)

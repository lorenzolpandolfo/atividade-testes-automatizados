from usuario import Usuario, ADMIN_USER

DEFAULT_USERS = [ADMIN_USER]

class Banco:
    def __init__(self, usuarios: list = DEFAULT_USERS):
        self.usuarios = usuarios

    def registrar_usuario(self, usuario: Usuario) -> None:
        if self.validar_usuario(usuario):
            self.usuarios.append(usuario)
    
    def validar_usuario(self, usuario: Usuario) -> bool:
        return usuario.idade > 18

    def bloquear_usuario(self, usuario: Usuario) -> None:
        if usuario.ativo:
            usuario.ativo = False
    
    def desbloquear_usuario(self, usuario: Usuario) -> None:
        if not usuario.ativo:
            usuario.ativo = True
    

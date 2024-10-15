import pytest
from usuario import Usuario, Banco

@pytest.fixture
def banco():
    """Fixture para criar uma instância do Banco antes de cada teste."""
    return Banco()

@pytest.fixture
def usuario_valido():
    return Usuario('Carlos', 'senha123', 25, 1000, 1500)

@pytest.fixture
def usuario_invalido():
    return Usuario('João', 'senha123', 16, 500, 1000)

@pytest.fixture
def usuario_bloqueado():
    usuario = Usuario('Maria', 'senha123', 22, 800, 1200)
    banco = Banco()
    banco.bloquear_usuario(usuario)
    return usuario


def test_registrar_usuario_valido(banco, usuario_valido):
    """Teste para registrar um usuário válido."""

    banco.registrar_usuario(usuario_valido)
    assert usuario_valido in banco.usuarios


def test_registrar_usuario_invalido(banco, usuario_invalido):
    """Teste para não registrar um usuário inválido (menor de idade)."""

    banco.registrar_usuario(usuario_invalido)
    assert usuario_invalido not in banco.usuarios


def test_bloquear_usuario(banco, usuario_valido):
    """Teste para bloquear um usuário ativo."""

    banco.bloquear_usuario(usuario_valido)
    assert not usuario_valido.ativo


def test_desbloquear_usuario(banco, usuario_bloqueado):
    """Teste para desbloquear um usuário bloqueado."""

    banco.desbloquear_usuario(usuario_bloqueado)
    assert usuario_bloqueado.ativo


def test_validar_usuario_menor_idade(banco, usuario_invalido):
    """Teste para validar usuário menor de idade."""

    is_valid = banco.validar_usuario(usuario_invalido)
    assert not is_valid


def test_validar_usuario_maior_idade(banco, usuario_valido):
    """Teste para validar usuário maior de idade."""

    is_valid = banco.validar_usuario(usuario_valido)
    assert is_valid

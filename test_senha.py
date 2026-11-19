from senha import senha_valida


def test_senha_com_exatamente_14_caracteres_e_aceita():
    senha = "a" * 14
    resultado = senha_valida(senha)
    assert resultado is True


def test_senha_com_13_caracteres_e_rejeitada():
    senha = "a" * 13
    resultado = senha_valida(senha)
    assert resultado is False


def test_senha_vazia_e_rejeitada():
    senha = ""
    resultado = senha_valida(senha)
    assert resultado is False

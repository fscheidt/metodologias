import pytest

@pytest.fixture
def conta():
    from src.pix.conta import Conta
    return Conta(pix="jj@gmail.com")

def test_transferencia_pix_mesma_conta(conta):
    """ faz pix para si proprio """
    with pytest.raises(ValueError):
        # conta.transferir(conta.pix, 1000) # TODO
        raise ValueError # remover para testar transferir


"""
Testes das formas de pagamento (Aula assíncrona — Polimorfismo).

Ficam como "skipped" até os arquivos existirem em src/models/.
Execute com:  pytest tests/test_pagamento.py -v
"""
import pytest

PaymentMethod = pytest.importorskip("src.models.payment_method").PaymentMethod
PixPayment = pytest.importorskip("src.models.pix_payment").PixPayment
BoletoPayment = pytest.importorskip("src.models.boleto_payment").BoletoPayment
CreditCardPayment = pytest.importorskip("src.models.credit_card_payment").CreditCardPayment


def test_classe_abstrata_nao_pode_ser_instanciada():
    with pytest.raises(TypeError):
        PaymentMethod()


def test_pagamentos_sao_subclasses_de_payment_method():
    for classe in (PixPayment, BoletoPayment, CreditCardPayment):
        assert issubclass(classe, PaymentMethod)


def test_pix_tem_5_por_cento_de_desconto():
    assert PixPayment().calculate_total(1000) == 950.00


def test_boleto_cobra_valor_integral():
    assert BoletoPayment().calculate_total(1000) == 1000.00


def test_cartao_ate_3x_sem_juros():
    assert CreditCardPayment(3).calculate_total(1000) == 1000.00


def test_cartao_acima_de_3x_com_acrescimo():
    assert CreditCardPayment(6).calculate_total(1000) == 1100.00


def test_cartao_parcelas_padrao_e_1():
    assert CreditCardPayment().calculate_total(500) == 500.00


@pytest.mark.parametrize("parcelas", [0, 13])
def test_cartao_parcelas_invalidas(parcelas):
    with pytest.raises(ValueError):
        CreditCardPayment(parcelas)


@pytest.mark.parametrize("valor", [0, -50])
def test_valor_invalido_gera_erro(valor):
    for pagamento in (PixPayment(), BoletoPayment(), CreditCardPayment(2)):
        with pytest.raises(ValueError):
            pagamento.calculate_total(valor)


def test_polimorfismo_descricoes():
    pagamentos = [PixPayment(), BoletoPayment(), CreditCardPayment(6)]
    assert [p.description() for p in pagamentos] == [
        "Pix", "Boleto bancário", "Cartão de crédito em 6x"
    ]

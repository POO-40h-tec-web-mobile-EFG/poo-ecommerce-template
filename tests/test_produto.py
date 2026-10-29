"""
Testes da classe Product (Aula 2).

Enquanto o arquivo src/models/product.py não existir, estes testes ficam
como "skipped" (pulados). Depois que você criar a classe, eles passam a rodar.
"""
import pytest

product_module = pytest.importorskip("src.models.product")
Product = product_module.Product


def test_criar_produto():
    produto = Product("Notebook", 3500.0)
    assert produto.name == "Notebook"
    assert produto.price == 3500.0


def test_preco_negativo_gera_erro():
    with pytest.raises(ValueError):
        Product("Mouse", -10.0)

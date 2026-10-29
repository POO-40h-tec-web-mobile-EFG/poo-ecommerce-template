"""
Testes da Aula 1: garantem que a estrutura do projeto está correta.
Execute na raiz do projeto com:  pytest
"""
from pathlib import Path
import importlib

RAIZ = Path(__file__).resolve().parent.parent


def test_pastas_obrigatorias_existem():
    for pasta in ["docs", "src/models", "src/services",
                  "src/repositories", "src/exceptions", "tests", "data"]:
        assert (RAIZ / pasta).is_dir(), f"Pasta ausente: {pasta}"


def test_pacotes_podem_ser_importados():
    for pacote in ["src", "src.models", "src.services",
                   "src.repositories", "src.exceptions", "src.main"]:
        importlib.import_module(pacote)


def test_readme_foi_preenchido_pelo_aluno():
    readme = (RAIZ / "README.md").read_text(encoding="utf-8")
    preenchido = "Seu Nome Aqui" not in readme
    assert preenchido, (
        "Atualize a seção 'Sobre mim' do README com seu nome (entregável da Aula 1)."
    )

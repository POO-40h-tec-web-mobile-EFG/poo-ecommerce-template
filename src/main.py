"""
Ponto de entrada do sistema.

Execute a partir da RAIZ do projeto:
    python -m src.main
"""

MENU = """
========================================
        LOJA POO — Backend Python
========================================
 1 - Produtos e categorias   (Aula 2)
 2 - Clientes e endereços    (Aula 3)
 3 - Carrinho de compras     (Aula 4)
 4 - Pedidos                 (Aula 5)
 0 - Sair
========================================"""


def main() -> None:
    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Até a próxima!")
            break
        elif opcao in {"1", "2", "3", "4"}:
            print("\n>> Funcionalidade ainda não implementada. Vamos construir nas próximas aulas!")
        else:
            print("\n>> Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

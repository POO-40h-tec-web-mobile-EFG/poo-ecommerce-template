"""
services — Regras de negócio.

Classes que coordenam os objetos de domínio para executar uma ação do sistema.
Exemplo: CartService (adicionar item, calcular total), OrderService (finalizar pedido).

Os services usam os models e os repositories, mas NÃO fazem print/input:
quem conversa com o usuário é o main.py.
"""

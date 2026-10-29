# 📋 Requisitos do sistema

O sistema é o **backend** de uma loja virtual, operado pelo terminal (menu em `src/main.py`).

## Requisitos funcionais (RF)

| ID | Requisito | Aula |
|---|---|---|
| RF01 | Cadastrar categorias de produtos | 2 |
| RF02 | Cadastrar produtos com nome, preço, estoque e categoria | 2 |
| RF03 | Listar produtos cadastrados | 2 |
| RF04 | Cadastrar clientes com nome, e-mail e CPF | 3 |
| RF05 | Associar um ou mais endereços a um cliente | 3 |
| RF06 | Adicionar produto ao carrinho informando a quantidade | 4 |
| RF07 | Remover produto do carrinho | 4 |
| RF08 | Listar itens do carrinho com subtotal e total | 4 |
| RF09 | Finalizar pedido a partir do carrinho | 5 |
| RF10 | Listar pedidos de um cliente | 5 |
| RF13 | Calcular o total da compra conforme a forma de pagamento (Pix, boleto ou cartão) | Assíncrona |
| RF11 | Salvar e carregar produtos, clientes e pedidos em JSON | 6 |
| RF12 | Exibir mensagens de erro claras para operações inválidas | 6 |

## Requisitos não funcionais (RNF)

| ID | Requisito |
|---|---|
| RNF01 | O sistema deve ser escrito em Python 3.10 ou superior |
| RNF02 | O código deve seguir o paradigma orientado a objetos (uma classe por arquivo em `src/models`) |
| RNF03 | Atributos das classes devem ser encapsulados (uso de `_atributo` e `@property`) |
| RNF04 | Os dados devem ser persistidos em arquivos JSON na pasta `data/` |
| RNF05 | O projeto deve ter testes automatizados executáveis com `pytest` |
| RNF06 | O código deve estar versionado no GitHub com commits frequentes e descritivos |

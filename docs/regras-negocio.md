# ⚖️ Regras de negócio

| ID | Regra | Onde aplicar |
|---|---|---|
| RN01 | O preço de um produto deve ser maior que zero | `Product` |
| RN02 | O estoque de um produto não pode ser negativo | `Product` |
| RN03 | Todo produto pertence a exatamente uma categoria | `Product` / `Category` |
| RN04 | O e-mail do cliente deve conter `@` | `Customer` |
| RN05 | Um cliente pode ter vários endereços, mas pelo menos um para fechar pedido | `Customer` / `Order` |
| RN06 | A quantidade de um item no carrinho deve ser maior que zero | `CartItem` |
| RN07 | Não é possível adicionar ao carrinho quantidade maior que o estoque | `Cart` |
| RN08 | Adicionar um produto que já está no carrinho soma a quantidade | `Cart` |
| RN09 | Não é possível finalizar pedido com carrinho vazio | `Order` / serviço de pedido |
| RN10 | Ao finalizar o pedido, o estoque dos produtos é reduzido | serviço de pedido |
| RN11 | O preço do item no pedido é fixado no momento da compra | `OrderItem` |
| RN12 | Após finalizar o pedido, o carrinho é esvaziado | serviço de pedido |
| RN13 | Pagamento via Pix tem 5% de desconto | `PixPayment` |
| RN14 | Pagamento via boleto é cobrado pelo valor integral | `BoletoPayment` |
| RN15 | Cartão de crédito: até 3x sem acréscimo; acima de 3x, acréscimo de 10% | `CreditCardPayment` |
| RN16 | O valor a pagar deve ser maior que zero | `PaymentMethod` |
| RN17 | O cartão de crédito aceita de 1 a 12 parcelas | `CreditCardPayment` |

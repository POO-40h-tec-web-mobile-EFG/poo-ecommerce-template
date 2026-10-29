# ⚖️ Regras de negócio: as regras da loja

**Regra de negócio** é uma regra que a loja segue no mundo real e que o sistema precisa respeitar.

> Exemplo do dia a dia: "não dá para vender um produto que acabou no estoque".

## Regras da nossa loja

| Nº | Regra | Por quê? |
|---|---|---|
| 1 | O preço de um produto precisa ser **maior que zero** | Ninguém vende de graça (nem com preço negativo!) |
| 2 | Todo produto pertence a **uma categoria** | Para organizar a loja |
| 3 | O e-mail do cliente precisa ter **@** | Para não cadastrar e-mail errado |
| 4 | Não dá para colocar no carrinho **mais unidades do que tem no estoque** | Não dá para vender o que não existe |
| 5 | Se o produto já está no carrinho, a quantidade **aumenta** (não duplica) | Para o carrinho ficar organizado |
| 6 | Não dá para finalizar pedido com o **carrinho vazio** | Não existe pedido sem produto |
| 7 | Depois que o pedido é finalizado, o **carrinho fica vazio** | Para começar uma nova compra |
| 8 | Pagamento no **Pix tem 5% de desconto** | Para incentivar o Pix |
| 9 | Pagamento no **cartão tem 10% de acréscimo** | Por causa das taxas do cartão |

💡 **Dica:** no código, essas regras quase sempre viram um `if`. Por exemplo:

```python
if price <= 0:
    print("Erro: o preço precisa ser maior que zero!")
```

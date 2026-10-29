# 🧩 Diagrama de classes (produto final esperado)

Este é o modelo que vamos construir até a Aula 7. O GitHub desenha o diagrama automaticamente a partir do código Mermaid abaixo.

```mermaid
classDiagram
    class User {
        -name: str
        -email: str
    }

    class Customer {
        -cpf: str
        -addresses: list~Address~
        +add_address(address)
    }

    class Address {
        -street: str
        -number: str
        -city: str
        -state: str
        -zip_code: str
    }

    class Category {
        -name: str
        -description: str
    }

    class Product {
        -name: str
        -price: float
        -stock: int
        -category: Category
        +decrease_stock(quantity)
    }

    class Cart {
        -customer: Customer
        -items: list~CartItem~
        +add_product(product, quantity)
        +remove_product(product)
        +total() float
        +clear()
    }

    class CartItem {
        -product: Product
        -quantity: int
        +subtotal() float
    }

    class Order {
        -customer: Customer
        -items: list~OrderItem~
        -created_at: datetime
        -status: str
        -payment: PaymentMethod
        +total() float
    }

    class OrderItem {
        -product: Product
        -quantity: int
        -unit_price: float
        +subtotal() float
    }

    class PaymentMethod {
        <<abstract>>
        +calculate_total(amount)* float
        +description()* str
    }

    class PixPayment {
        +calculate_total(amount) float
        +description() str
    }

    class BoletoPayment {
        +calculate_total(amount) float
        +description() str
    }

    class CreditCardPayment {
        -installments: int
        +calculate_total(amount) float
        +description() str
    }

    PaymentMethod <|-- PixPayment : polimorfismo
    PaymentMethod <|-- BoletoPayment
    PaymentMethod <|-- CreditCardPayment
    Order --> "1" PaymentMethod

    User <|-- Customer : herança (É-UM)
    Customer *-- "1..*" Address : composição (TEM-UM)
    Product --> "1" Category
    Cart --> "1" Customer
    Cart *-- "0..*" CartItem
    CartItem --> "1" Product
    Order --> "1" Customer
    Order *-- "1..*" OrderItem
    OrderItem --> "1" Product
```

## Legenda

| Símbolo | Significado |
|---|---|
| `-` | atributo privado/protegido (em Python: `_atributo`) |
| `+` | público |
| `<|--` | herança: `Customer` **é um** `User` |
| `*--` | composição: a parte não existe sem o todo |
| `<<abstract>>` / `*` | classe abstrata / método abstrato (as subclasses são obrigadas a implementar) |
| `-->` | associação: um objeto conhece/usa o outro |

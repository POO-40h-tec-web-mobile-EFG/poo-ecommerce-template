# Aula Assíncrona — Polimorfismo e Classes Abstratas

📅 **Liberação:** 14/11/2026 (sábado) · ⏰ **Prazo de entrega:** 16/11/2026 (segunda), 23h59 · ⌛ **Carga horária:** 3h

Esta aula é feita **no seu ritmo**, fora da sala. Siga as etapas na ordem e, se travar, abra uma Issue do tipo **Dúvida** no seu repositório.

---

## 🎯 Objetivos
- Entender o que é **polimorfismo**: o mesmo método com comportamentos diferentes em cada classe.
- Criar uma **classe abstrata** com o módulo `abc` do Python.
- Aplicar **sobrescrita de métodos** (*override*) em subclasses.
- Implementar as formas de pagamento da loja.

---

## Etapa 1 — Conceitos (≈ 30 min)

### Polimorfismo
"Poli" = muitas, "morfo" = formas. É quando objetos de classes diferentes respondem à **mesma chamada de método**, cada um do seu jeito.

Na loja: todo pagamento sabe `calculate_total()`, mas o Pix dá desconto, o boleto cobra o valor cheio e o cartão pode ter juros. Quem chama o método **não precisa saber qual é o tipo** do pagamento.

### Classe abstrata
É uma classe que **serve de molde** e **não pode ser instanciada**. Ela define *o que* as subclasses devem ter, mas não *como*.

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

Forma()   # ❌ TypeError: Can't instantiate abstract class Forma
```

### Sobrescrita (override) × Sobrecarga (overload)
| | Sobrescrita | Sobrecarga |
|---|---|---|
| O que é | Subclasse redefine um método da superclasse | Mesmo método com parâmetros diferentes |
| Em Python | ✅ Comum | ⚠️ Não existe como em Java — usamos **parâmetros com valor padrão** |

```python
# "Sobrecarga" no estilo Python: parâmetro opcional
def calcular_frete(peso, expresso=False):
    return peso * (2.0 if expresso else 1.0)
```

📖 Leitura de apoio: [Tutorial Python — Classes (herança)](https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance) e [módulo abc](https://docs.python.org/pt-br/3/library/abc.html).

---

## Etapa 2 — Exemplo resolvido (≈ 30 min)

Leia, copie para um arquivo de rascunho (fora do `src/`) e execute.

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    """Classe abstrata: toda notificação precisa saber se enviar."""

    def __init__(self, recipient: str):
        self._recipient = recipient

    @abstractmethod
    def send(self, message: str) -> str:
        ...


class EmailNotification(Notification):
    def send(self, message: str) -> str:          # sobrescrita
        return f"[E-MAIL para {self._recipient}] {message}"


class SmsNotification(Notification):
    def send(self, message: str) -> str:          # sobrescrita
        return f"[SMS para {self._recipient}] {message[:20]}..."


# Polimorfismo: a mesma chamada, comportamentos diferentes
notificacoes = [
    EmailNotification("maria@email.com"),
    SmsNotification("(62) 99999-0000"),
]
for n in notificacoes:
    print(n.send("Seu pedido foi enviado!"))
```

✏️ **Teste você mesmo:** crie uma `WhatsappNotification` e adicione à lista. Repare que o `for` **não precisou mudar**. Isso é extensibilidade!

---

## Etapa 3 — Exercício no projeto (≈ 1h30)

Implemente as **formas de pagamento** da loja em `src/models/`, **uma classe por arquivo**:

| Arquivo | Classe | Regra de `calculate_total(amount)` | `description()` retorna |
|---|---|---|---|
| `payment_method.py` | `PaymentMethod` (abstrata) | método abstrato | método abstrato |
| `pix_payment.py` | `PixPayment` | 5% de desconto (RN13) | `"Pix"` |
| `boleto_payment.py` | `BoletoPayment` | valor integral (RN14) | `"Boleto bancário"` |
| `credit_card_payment.py` | `CreditCardPayment` | até 3x: valor integral; acima de 3x: +10% (RN15) | `"Cartão de crédito em Nx"` |

Requisitos:
1. `PaymentMethod` herda de `ABC` e tem `calculate_total` e `description` como `@abstractmethod`.
2. `calculate_total` deve lançar `ValueError` se `amount` for menor ou igual a zero (RN16). Dica: coloque essa validação num método **concreto** da classe abstrata e reutilize nas subclasses.
3. `CreditCardPayment` recebe `installments` (parcelas) no construtor, com valor padrão `1`, e só aceita de 1 a 12 parcelas (RN17). Fora disso: `ValueError`.
4. Valores arredondados com 2 casas decimais: `round(valor, 2)`.
5. No `main.py`, adicione uma demonstração que percorre uma lista com os três pagamentos e imprime a descrição e o total para uma compra de R$ 1.000,00.

Saída esperada da demonstração:
```
Pix: R$ 950.00
Boleto bancário: R$ 1000.00
Cartão de crédito em 6x: R$ 1100.00
```

---

## Etapa 4 — Testar (≈ 15 min)

```bash
pytest tests/test_pagamento.py -v
```
Enquanto os arquivos não existirem, os testes aparecem como **SKIPPED**. Depois de criá-los, todos devem ficar **PASSED** ✅.

---

## Etapa 5 — Reflexão (≈ 15 min)

Crie o arquivo `docs/reflexao-polimorfismo.md` e responda com suas palavras (3 a 5 linhas cada):

1. Por que não faz sentido criar um objeto `PaymentMethod()` diretamente?
2. Se a loja passar a aceitar **criptomoeda**, quais arquivos você precisaria criar ou alterar? E quais **não** precisaria mexer?
3. Dê um exemplo, fora do e-commerce, de polimorfismo no mundo real.

---

## 📦 Entrega (até 16/11, 23h59)

- [ ] 4 arquivos de pagamento em `src/models/`
- [ ] Demonstração no `main.py`
- [ ] `pytest` passando
- [ ] `docs/reflexao-polimorfismo.md` respondido
- [ ] Commit e push: `git commit -m "feat: entrega assíncrona - polimorfismo em pagamentos"`
- [ ] Issue **Entrega de aula** aberta com o link do commit

## ✅ Como será avaliado
| Item | Peso |
|---|---|
| Classe abstrata correta (`ABC` + `@abstractmethod`) | 30% |
| Sobrescrita e regras de cada pagamento | 30% |
| Testes passando | 15% |
| Reflexão | 15% |
| Commit e Issue no prazo | 10% |

Na **Aula 6 (17/11)** vamos usar esses pagamentos para finalizar pedidos — então não deixe para depois! 😉

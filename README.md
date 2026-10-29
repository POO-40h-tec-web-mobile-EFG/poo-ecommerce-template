# 🛒 Loja POO — Backend de E-commerce em Python

Projeto da disciplina **Programação Orientada a Objetos (40h)** — Curso Técnico em Desenvolvimento de Sistemas.

Ao longo de 7 encontros presenciais e 1 aula assíncrona, cada aluno vai construir **individualmente** o backend de uma loja virtual em Python, aplicando classes, objetos, encapsulamento, composição, herança, polimorfismo, persistência em JSON, exceções e testes.

> ⚠️ Este repositório é o **template** da disciplina. Não faça commits aqui: crie o **seu** repositório a partir dele (passo 1 abaixo).

---

## 👤 Sobre mim

> Entregável da Aula 1: substitua os dados abaixo pelos seus e faça commit.

- **Nome:** Seu Nome Aqui
- **Turma:** 
- **GitHub:** https://github.com/seu-usuario
- **O que espero aprender nesta disciplina:** 

---

## 🚀 Como começar

### 1. Criar o seu repositório a partir do template
1. Na página deste repositório, clique em **Use this template → Create a new repository**.
2. Owner: a organização da turma (ou sua conta, conforme orientação da professora).
3. Nome: `ecommerce-python-seunome` (ex.: `ecommerce-python-maria`).
4. Clique em **Create repository**.

### 2. Clonar e abrir no VS Code
```bash
git clone https://github.com/ORGANIZACAO/ecommerce-python-seunome.git
cd ecommerce-python-seunome
code .
```

### 3. Criar o ambiente virtual e instalar as dependências
```bash
python3 -m venv venv

# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

### 4. Executar o sistema
Sempre a partir da **raiz** do projeto:
```bash
python -m src.main
```

### 5. Executar os testes
```bash
pytest
```
Na Aula 1, o teste `test_readme_foi_preenchido_pelo_aluno` só passa depois que você preencher a seção **Sobre mim**. 😉

---

## 📁 Estrutura do projeto

```
ecommerce-python-seunome/
├── data/                 # Arquivos JSON gerados pelo sistema (Aula 6)
├── docs/                 # Requisitos, regras de negócio, diagramas e entregas
│   └── aulas/            # Roteiro de cada encontro
├── src/
│   ├── models/           # Classes de domínio: Product, Customer, Cart, Order...
│   ├── services/         # Regras de negócio
│   ├── repositories/     # Leitura e gravação em JSON
│   ├── exceptions/       # Exceções customizadas
│   └── main.py           # Ponto de entrada (menu do sistema)
├── tests/                # Testes com pytest
├── requirements.txt
└── README.md
```

---

## 🔁 Fluxo de trabalho com Git

A cada funcionalidade concluída:
```bash
git status                      # o que mudou?
git add .                       # preparar as mudanças
git commit -m "feat: cria classe Product"
git push                        # enviar para o GitHub
```

**Padrão de mensagens de commit**

| Prefixo | Quando usar | Exemplo |
|---|---|---|
| `feat:` | nova funcionalidade | `feat: adiciona cálculo do total do carrinho` |
| `fix:` | correção de erro | `fix: impede preço negativo em Product` |
| `docs:` | documentação | `docs: atualiza README com meus dados` |
| `test:` | testes | `test: cria testes de Cart` |
| `refactor:` | melhoria sem mudar comportamento | `refactor: extrai OrderService` |

> 📌 O histórico de commits é **evidência de participação**. Faça commits pequenos e frequentes — pelo menos um por aula.

---

## 📚 Documentação

- [Cronograma e entregas](docs/entregas.md)
- [Requisitos](docs/requisitos.md)
- [Regras de negócio](docs/regras-negocio.md)
- [Diagrama de classes](docs/diagrama-classes.md)
- [Critérios de avaliação](docs/criterios-avaliacao.md)
- [Roteiro da Aula 1](docs/aulas/aula-01-kickoff.md)
- [Aula assíncrona — Polimorfismo (14/11)](docs/aulas/aula-assincrona-polimorfismo.md)

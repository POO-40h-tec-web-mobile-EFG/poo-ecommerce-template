# Aula 1: Conhecendo o projeto e o GitHub (29/10)

## 🎯 Hoje você vai
- Criar o **seu** repositório do projeto
- Abrir o projeto no VS Code
- Executar o seu primeiro programa
- Fazer o seu primeiro **commit**

---

## Passo 1: Criar o seu repositório
1. Abra o link do template que a professora passou.
2. Clique no botão verde **Use this template → Create a new repository**.
3. Em **Repository name**, escreva: `ecommerce-python-seunome` (ex.: `ecommerce-python-maria`)
4. Clique em **Create repository**.

## Passo 2: Abrir no VS Code
1. No seu repositório no GitHub, clique no botão verde **Code** e copie o link.
2. Abra o VS Code e aperte `Ctrl + Shift + P`.
3. Digite **Git: Clone**, aperte Enter e cole o link.
4. Escolha uma pasta no computador e clique em **Open** quando ele perguntar.

## Passo 3: Configurar o Git (só na primeira vez)
No terminal do VS Code (**Terminal → New Terminal**), digite (com o seu nome e e-mail do GitHub):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```

## Passo 4: Executar o programa
No terminal, digite:

```bash
python3 src/main.py
```

Deve aparecer a mensagem de boas-vindas da loja. 🎉

## Passo 5: Colocar o seu nome
1. Abra `src/main.py` e troque `Seu Nome Aqui` pelo seu nome.
2. Execute de novo e veja o seu nome aparecer.
3. Abra o `README.md` e preencha a parte **Sobre mim**.

## Passo 6: Fazer o primeiro commit
1. Clique no ícone **Source Control** (barra da esquerda).
2. Mensagem: `Aula 1 - meu primeiro commit`
3. Clique em **Commit** e depois em **Sync Changes**.
4. Abra o seu repositório no GitHub e confira se as mudanças apareceram. ✅

---

## 💭 Para pensar
Pense numa loja online que você usa:
- Que **coisas** existem nela? (produto, cliente...)
- Que **informações** um produto tem?

Vamos usar suas respostas na Aula 2!

## 📦 Entrega
Repositório criado no GitHub, com o seu nome no `main.py` e no `README.md`.

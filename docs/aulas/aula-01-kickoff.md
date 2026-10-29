# Aula 1 — Kickoff e GitHub (29/10/2026)

## 🎯 Objetivos
- Conhecer o produto final: o backend de uma loja virtual orientada a objetos.
- Entender a diferença entre o **template** (da professora) e o **seu repositório**.
- Praticar o fluxo `clone → editar → add → commit → push`.

## 🧠 Conceitos do dia
- **Paradigma orientado a objetos:** o sistema é formado por objetos que têm **dados** (atributos) e **comportamentos** (métodos).
- **Git:** controle de versão no seu computador.
- **GitHub:** onde o repositório fica publicado e onde a professora acompanha suas entregas.
- **Repositório template:** um modelo que gera cópias independentes.

## 🛠️ Atividade prática
1. [ ] Criar o repositório `ecommerce-python-seunome` a partir do template (**Use this template**).
2. [ ] Clonar o repositório e abri-lo no VS Code.
3. [ ] Criar o ambiente virtual e instalar as dependências (`pip install -r requirements.txt`).
4. [ ] Executar o sistema: `python -m src.main`.
5. [ ] Executar os testes: `pytest` (um teste vai falhar — é de propósito!).
6. [ ] Preencher a seção **Sobre mim** do `README.md`.
7. [ ] Rodar `pytest` de novo e ver todos os testes passando ✅.
8. [ ] Fazer o commit e o push:
   ```bash
   git add .
   git commit -m "docs: atualiza README com meus dados"
   git push
   ```
9. [ ] Abrir uma Issue **Entrega de aula** com o checklist da Aula 1.

## 💭 Desafio de modelagem (para discutir em sala)
Olhando para uma loja virtual que você usa, responda:
- Quais **objetos** existem? (ex.: produto, cliente...)
- Que **atributos** um produto tem?
- Que **ações** um carrinho de compras executa?

Anote suas respostas — vamos usá-las na Aula 2.

## 📦 Entregável
Repositório individual publicado no GitHub com o README atualizado.

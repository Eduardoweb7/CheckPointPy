# 🐍 Sistema de Cadastro com Listas em Python

Projeto desenvolvido como avaliação na **FIAP** para a disciplina de Python.

**Aluno:** Eduardo Barbosa da Silva  
**RM:** 568327

---

## 📋 Descrição

Projeto composto por dois sistemas de cadastro independentes desenvolvidos em Python, utilizando listas de dicionários para armazenamento em memória. Ambos implementam um menu interativo com as operações de **CRUD** (inserir, alterar, excluir e exibir), além de relatórios com filtros específicos.

---

## 🗂️ Estrutura do Projeto

```
├── questao1.py   # Sistema de cadastro de funcionários
└── questao2.py   # Sistema de cadastro de medicamentos
```

---

## 👔 Questão 1 — Sistema de Funcionários

Gerencia o cadastro de funcionários com cálculo automático de descontos e salário líquido.

### Dados armazenados por funcionário
- Código, Nome, CPF
- Data de nascimento (dia, mês, ano)
- Cargo
- Salário bruto, Desconto INSS (15%), Desconto IR (18,95%), Salário líquido

### Funcionalidades
| Opção | Descrição |
|-------|-----------|
| 1 | Inserir funcionário |
| 2 | Alterar funcionário |
| 3 | Excluir funcionário |
| 4 | Exibir dados de um funcionário |
| 5 | Relatório: nascidos a partir de 1989 com salário líquido entre R$ 8.000 e R$ 15.000 |
| 7 | Relatório: Cientistas de Dados com salário bruto acima de R$ 14.000 |

---

## 💊 Questão 2 — Sistema de Medicamentos

Gerencia o cadastro de medicamentos com cálculo automático do valor de venda.

### Dados armazenados por medicamento
- Código, Descrição
- Data de validade (dia, mês, ano)
- Valor de compra, Valor de venda (markup de 30%)

### Funcionalidades
| Opção | Descrição |
|-------|-----------|
| 1 | Inserir medicamento |
| 2 | Alterar medicamento |
| 3 | Excluir medicamento |
| 4 | Exibir dados de um medicamento |
| 5 | Relatório: medicamentos com ano de validade superior a 2025 |
| 7 | Relatório: medicamentos com valor de compra entre R$ 120,00 e R$ 450,00 |

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.x instalado.

```bash
# Executar o sistema de funcionários
python questao1.py

# Executar o sistema de medicamentos
python questao2.py
```

---

## 💡 Conceitos Aplicados

- Listas de dicionários para estruturação de dados
- Funções com separação de responsabilidades
- Tratamento de exceções com `try/except/else/finally`
- Busca por índice e manipulação de listas
- Menus interativos com laços `while`
- Relatórios com filtros e critérios combinados

---

## 🏫 Instituição

**FIAP** — Faculdade de Informática e Administração Paulista

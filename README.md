# 📖 Biblioteca Página Virada

Sistema em Python (CLI) para controle de acervo, cadastro de livros, empréstimos e estatísticas da **Biblioteca Página Virada**.

Tudo roda no terminal, com um menu simples e os dados salvos em um arquivo JSON local.

---

## ✨ Funcionalidades

- **Cadastrar livro**: título, autor, gênero e ano de publicação. O sistema gera automaticamente um código único e uma mensagem com emoji de acordo com o gênero.
- **Buscar livro por código**: consulta rápida de todas as informações de um livro.
- **Registrar empréstimo / devolução**: controla se o livro está disponível (`D`) ou emprestado (`E`).
- **Estatísticas do acervo**: total de livros, quantos estão disponíveis e emprestados, contagem por gênero e o gênero mais frequente.
- **Persistência de dados**: o acervo é salvo em `acervo.json` a cada novo cadastro.

---

## 🛠️ Requisitos

- **Python 3.14 ou superior** (o projeto usa `match/case` e a sintaxe `except A, B:` sem parênteses)
- Biblioteca [`emoji`](https://pypi.org/project/emoji/)
- **Windows** (o menu usa `os.system("cls")` para limpar a tela)

---

## 🚀 Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/samykuroda/pagina-virada-library.git
   cd pagina-virada-library
   ```

2. Instale a dependência:

   ```bash
   pip install emoji
   ```

3. Execute o programa:

   ```bash
   python main.py
   ```

---

## 🧭 Como usar

Ao iniciar, o menu principal é exibido:

```
MENU PRINCIPAL

1- Cadastrar livro
2- Buscar livro por código
3- Registrar empréstimo / devolução
4- Ver estatísticas do acervo
5- Sair
```

| Opção | O que faz |
|-------|-----------|
| **1** | Pede título, autor, gênero e ano. Gera o código, cadastra o livro como disponível e salva no `acervo.json`. |
| **2** | Pede o código do livro e exibe os dados dele (ou "Livro não encontrado"). |
| **3** | Pede o código do livro. Se estiver disponível, pede o nome de quem está pegando emprestado. Se estiver emprestado, pergunta se é uma devolução. |
| **4** | Mostra total de livros, disponíveis, emprestados, contagem por gênero e o gênero com mais livros. |
| **5** | Encerra o programa. |

### Código do livro

O código é gerado assim:

> 3 primeiras letras do título (sem espaços) + 3 primeiras letras do sobrenome do autor + 2 últimos dígitos do ano

Exemplo: *O Hobbit*, de *J. R. R. Tolkien*, publicado em *1937* → `OHOTOL37`

### Gêneros com emoji

Alguns gêneros ganham um emoji próprio no cadastro:

| Gênero | Emoji |
|--------|-------|
| Romance | 💓 |
| Terror | 👻 |
| Fantasia | 🪄 |
| Ficção | 👾 |
| Drama | 😭 |
| Outros | 📖 |

---

## 🗂️ Estrutura do projeto

```
pagina-virada-library/
├── main.py         # Menu principal e fluxo do programa
├── functions.py    # Funções auxiliares (código, emojis, JSON, busca e estatísticas)
├── .gitignore
└── acervo.json     # Gerado automaticamente ao cadastrar o primeiro livro
```

### Formato de um livro no `acervo.json`

```json
{
    "titulo": "O hobbit",
    "autor": "J. r. r. tolkien",
    "genero": "Fantasia",
    "ano": 1937,
    "codigo": "OHOTOL37",
    "mensagem": "FANTASIA 🪄",
    "status": "D"
}
```

---

## 🔮 Ideias para o futuro

- Remover e editar livros
- Registrar quem pegou cada livro emprestado e a data de devolução
- Busca por título, autor ou gênero
- Suporte a Linux e macOS (limpar a tela de forma multiplataforma)

---

## 👩‍💻 Autora

Feito por [Samy Kuroda](https://github.com/samykuroda).

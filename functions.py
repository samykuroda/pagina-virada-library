import json

def gera_codigo(titulo, autor, ano):
    titulo_sem_espaco = titulo.replace(" ", "").upper()
    lista_autor = autor.upper().split()
    sobrenome = lista_autor[-1]
    codigo = titulo_sem_espaco[:3] + sobrenome[:3] + str(ano)[-2:]
    return codigo
    
def emoji_gen(genero):
    import emoji
    match genero:
        case "ROMANCE":
            e_genero = emoji.emojize(f"{genero} :beating_heart:")
        case "TERROR":
            e_genero = emoji.emojize(f"{genero} :ghost:")
        case "FANTASIA":
            e_genero = emoji.emojize(f"{genero} :magic_wand:")
        case "FICÇÃO":
            e_genero = emoji.emojize(f"{genero} :alien_monster:")
        case "DRAMA":
            e_genero = emoji.emojize(f"{genero} :loudly_crying_face:")
        case _:
            e_genero = emoji.emojize(f"{genero} :open_book")
    return e_genero

def salvar_acervo(acervo):
    with open("acervo.json", "w", encoding="utf-8") as arquivo:
        json.dump(acervo, arquivo, ensure_ascii=False, indent=4)
        
def carregarAcervo():
    try:
        with open("acervo.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def busca_livro_codigo(buscar,acervo):
    for livro in acervo:
        if buscar == livro["codigo"]:
            return livro
        else:
            return "Livro não encontrado"

def livros_disponiveis(acervo):
    disponiveis = 0
    for i in acervo:
        if i["status"] == "D":
            disponiveis += 1
    return disponiveis

def livros_emprestados(acervo):
    emprestados = 0
    for i in acervo:
        if i["status"] == "E":
            emprestados += 1
    return emprestados

def analisar_acervo(acervo):
    if not acervo:
        print("O acervo está vazio!")
        return
    contagem = {}
    for livro in acervo:
        genero = livro["genero"]
        if genero in contagem:
            contagem[genero] += 1
        else:
            contagem[genero] = 1
    print("Contagem por gênero:")
    for genero, quantidade in contagem.items():
        print(f"- {genero}: {quantidade} livro(s)")
        
    mais_frequente = max(contagem, key=contagem.get)
    print(f"\nO gênero com mais livros é: {mais_frequente}")

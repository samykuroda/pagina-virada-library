# ============ ↳ 𐔌  BIBLIOTECA PÁGINA VIRADA  𐔌 ==========

import os
os.system('cls')
import time
import functions as f
    
acervo = f.carregarAcervo()

while True:
    os.system("cls")
    print(""" 
          MENU PRINCIPAL
          
          1- Cadastrar livro
          2- Buscar livro por código
          3- Registrar empréstimo / devolução
          4- Ver estatísticas de do acervo
          5- Sair
          """)
    try:
        opcao = int(input("Digite uma opcão do menu: "))
    except ValueError:
        print("Digite apenas o número da opção desejada!")
        input("ENTER para voltar para o menu...")
        continue
            
    match opcao:
        case 1:
            os.system("cls")
            titulo = input(f"Título do livro: ").capitalize().strip()
            autor = input(f"Nome do autor do livro: ").capitalize().strip()
            genero = input(f"Gênero do livro: ").upper().strip()
            while True:
                try:
                    ano = int(input(f"Ano de publicação: "))
                    break
                except ValueError, TypeError:
                    print("Só aceitamos número!")
            
            codigo = f.gera_codigo(titulo, autor, ano)
            mensagem = f.emoji_gen(genero)
            cadastro = {
                "titulo": titulo,
                "autor": autor,
                "genero": genero.capitalize(),
                "ano": ano,
                "codigo": codigo,
                "mensagem": mensagem,
                "status": "D"
            }
            acervo.append(cadastro)
            f.salvar_acervo(acervo)
            print("Livro cadastrado!")
            input("ENTER para voltar para o menu...")
                
        case 2:
            buscar = input("Digite o codigo do livro: ").upper()
            print(f.busca_livro_codigo(buscar,acervo))
            input("ENTER para voltar ao menu!")
        case 3:
            buscar = input("Digite o código do livro: ").upper().strip()
            encontrado = False

            for i in acervo:
                if buscar == i["codigo"]:
                    encontrado = True

                    if i["status"] == "D":
                        nome = input("Digite seu nome: ").capitalize()
                        i["status"] = "E"
                        print("Empréstimo registrado, boa leitura,", nome,"!")
                    else:
                        devolucao = input("É uma devolução? (s/n): ").lower().strip()
                        while devolucao not in ("s", "n"):
                            devolucao = input("Resposta inválida. Digite apenas 's' ou 'n': ").lower().strip()

                        if devolucao == "s":
                            i["status"] = "D"
                            print("Obrigada pela devolução, livro disponível novamente!")
                        else:
                            print("Nenhuma alteração feita.")
                    break

            if not encontrado:
                print("Código não encontrado.")

            input("ENTER para voltar ao menu.")
        
        case 4: #Estatisticas do acervo
            os.system("cls")
            print(f""" 
Quantidade de livros cadastrados: {len(acervo)} 
Livros disponíveis: {f.livros_disponiveis(acervo)}
Livros emprestados: {f.livros_emprestados(acervo)}      
            """)
            f.analisar_acervo(acervo)
            print()
            input("Digite ENTER para voltar ao menu!")
        case 5:
            os.system('cls')
            print("Saindo", end="")
            for i in range(1, 6):
                print(".", end="", flush=True)
                time.sleep(0.3) 
            break
        case _:
            print("Digite uma opção válida")
            
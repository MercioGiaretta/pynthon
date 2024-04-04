import os

def exibirLista(lista):
    print("Lista atual: ", lista)

def adicionarItem(lista):
    item = input("Digite o item que deseja adicionar: ")
    lista.append(item)
    exibirLista(lista)

def excluirItem(lista):
    item = input("Digite o item que deseja excluir: ")
    if item in lista:
        lista.remove(item)
        exibirLista(lista)
    else:
        print("Este item não está na lista.")

def gravarLista(lista):
    nome_arq = input("Digite o nome do Arquivo: ")
    with open(nome_arq,"w") as arquivo:
        for item in lista:
            arquivo.write(item + "\n")
    print("LISTA GRAVADO COM SUCESSO", {nome_arq})

    lista.sort(reversed = True)
    print("Lista ordenada com sucesso")

def listar_arquivos():
    diretorio = os.getcwd()
    arquivos = os.listdir(diretorio)
    print("Os arquivos desse diretorio são:")
    for lista_arquivos in arquivos:
        print(lista_arquivos) 

def carregar_arquivo(lista):

    nome_arquivo = input("Digite o nome do arquivo para carregar a lista:")
    try:
        with open (nome_arquivo, "r") as arquivo:
            lista.clear()
            for linha in arquivo:
                lista.append(linha.strip())
        print("Lista carregada com sucesso do arquivo" , nome_arquivo)
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro." , e)

def ordenar_lista(lista):
    lista.sort(reverse = True)
    print("Lista ordenada com sucesso!")


def principal():
    lista = []
    continuar = True

    while continuar:
        print("=-=-=-=Menu=-=-=-=")
        print("1 - Adicionar Item")
        print("2 - Excluir Item")
        print("3 - Exibir Lista")
        print("4 - Gravar Lista")
        print("5 - Listar Arquivos")
        print("6 - Carregar Lista")
        print("7 - Ordenar Lista")
        print("8 - Sair")

        opcoes = input("Digite o número da opção desejada: ")

        if opcoes == "1":
            adicionarItem(lista)
        elif opcoes == "2":
            excluirItem(lista)
        elif opcoes == "3":
            exibirLista(lista)
        elif opcoes == "4":
            gravarLista(lista)
        elif opcoes == "5":
            listar_arquivos()
        elif opcoes == "6":
            carregar_arquivo(lista)
        elif opcoes == "7":
            ordenar_lista(lista)
        elif opcoes == "8":
            continuar = False



        else:
            print("Opção inválida. Digite novamente.")

        print()

    print("Programa Encerrado.")

    

if __name__ == "__main__":
    principal()


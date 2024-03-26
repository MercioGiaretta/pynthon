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


def principal():
    lista = []
    continuar = True

    while continuar:
        print("=-=-=-=Menu=-=-=-=")
        print("1 - Adicionar Item")
        print("2 - Excluir Item")
        print("3 - Exibir Lista")
        print("4 - Gravar Lista")
        print("5 - Sair")

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
            continuar = False
        else:
            print("Opção inválida. Digite novamente.")

        print()

    print("Programa Encerrado.")

if __name__ == "__main__":
    principal()


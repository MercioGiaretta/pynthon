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

def principal():
    lista = []
    continuar = True

    while continuar:
        print("=-=-=-=Menu=-=-=-=")
        print("1 - Adicionar item")
        print("2 - Excluir item")
        print("3 - Exibir lista")
        print("4 - Sair")

        opcoes = input("Digite o número da opção desejada: ")

        if opcoes == "1":
            adicionarItem(lista)
        elif opcoes == "2":
            excluirItem(lista)
        elif opcoes == "3":
            exibirLista(lista)
        elif opcoes == "4":
            continuar = False
        else:
            print("Opção inválida. Digite novamente.")

        print()

    print("Programa Encerrado.")

if __name__ == "__main__":
    principal()


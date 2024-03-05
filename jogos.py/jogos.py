import forca
import adivinhacao

def escolha_jogos():
    print("=-=-=-=-=-=-=-=-=-=")
    print("=-Escolha o jogo-=")
    print("=-=-=-=-=-=-=-=-=-=")
    print("(1)Forca,(2)Adivinhação")
    jogo = int(input("Escolha o Jogo"))

    if(jogo == 1):
        print("Jogando força")
        forca.jogar()
    elif(jogo == 2):
        print("Jogano Adivinhação")
        adivinhacao.jogar_adivinhacao()
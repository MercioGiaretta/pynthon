import random

def jogar_jokenpo():
    vitorias = 0
    derrotas = 0
    opcoes = ["pedra", "papel", "tesoura"]
    print("Bem Vindo ao JoKenPo!!")
    print("Escolha: Pedra, Papel ou Tesoura.")

    while True:
        escolha_jogador = input("Sua Escolha:").lower()
        if escolha_jogador not in opcoes:
            print("Escolha inválida. Tente Novamente")
            continue

        escolha_comp = random.choice(opcoes)
        print(f"Computador escolheu  {escolha_comp}")

        if escolha_jogador == escolha_comp:
            print("Empate!")

        elif(
            (escolha_jogador=="papel" and escolha_comp == "pedra") or
            (escolha_jogador=="pedra" and escolha_comp == "tesoura") or
            (escolha_jogador=="tesoura" and escolha_comp == "papel")
        ):
            vitorias += 1
            print("Você Ganhou!")
        else:
            derrotas += 1
            print("Você Perdeu!")

        print(f"Você tem {vitorias} vitórias, e {derrotas} derrotas.")
        jogar_novamente = input("Você gostaria de jogar novamente porpetão?").lower()
        if jogar_novamente != "sim":
            break

if(__name__ == "__main__"):
    jogar_jokenpo()
import random

def jogar_jokenpo():
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

        jogar_novamente = input("Você gostaria de jogar novamente porpetão?").lower()
        if jogar_novamente != "sim":
            break

if(__name__ == "__main__"):
    jogar_jokenpo()
import random

def ganhador(escolha_jogador,escolha_comp):
    
        if escolha_jogador == escolha_comp:
            return "Empate!"
        elif (
            (escolha_jogador=="papel" and escolha_comp == "pedra") or
            (escolha_jogador=="pedra" and escolha_comp == "tesoura") or
            (escolha_jogador=="tesoura" and escolha_comp == "papel")
        ):
            return "Você Ganhou!"
        else:
            return "Você Perdeu!"

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    vitoria = 0
    derrota = 0
    print("Bem Vindo ao JoKenPo!!")
    print("Escolha: Pedra, Papel ou Tesoura.")

    while True:
        escolha_jogador = input("Sua Escolha:").lower()
        if escolha_jogador not in opcoes:
            print("Escolha inválida. Tente Novamente")
            continue

        escolha_comp = random.choice(opcoes)
        print(f"Computador escolheu {escolha_comp}")

        resultado = ganhador(escolha_jogador, escolha_comp)
        print(resultado)

        if resultado == "Você Venceu!":
            vitoria += 1
        elif resultado == "Você Perdeu!":
            derrota += 1
        print(f"Você tem {vitoria} vitórias, e {derrota} derrotas.")
        
        jogar_novamente = input("Você gostaria de jogar novamente porpetão?").lower()
        if jogar_novamente != "sim":
            break

if(__name__ == "__main__"):
    jogar_jokenpo()

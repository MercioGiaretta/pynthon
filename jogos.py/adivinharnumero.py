import random
numero_secreto = random.randint(1,10)
tentativa = 0
max_tentativa = 5
print("Bem vindo ao jogo de adivinhação")
print("Tente adivinhar o número secreto entre 1 e 10")

while tentativa < max_tentativa:
    palpite = int(input("Digite seu palpite"))
    
    tentativa += 1 
    
    if palpite == numero_secreto:
        print("Parabéns, você acertou o número secreto!!")
        break
    elif palpite > numero_secreto:
        print("O número secreto é menor. Tente novamente")
    else:
        print("O número secreto é maior. Tente novamente")
        
if tentativa < max_tentativa:
    print(f"Você acertou em {tentativa} tentativas")
else:
    print(f"Acabaram suas tentativas. O número correto era {numero_secreto}")
    
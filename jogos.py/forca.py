import jogos

def jogar():
    palavra_secreta = "maricatinga"
    letras_acertadas = ["_","_","_","_","_","_","_","_","_","_","_",]
    tentativas = 15


    while tentativas > 0 and "_" in letras_acertadas:
        palpite = input("Digite uma letra").lower()
        
        if palpite in palavra_secreta:
            index = 0
        for letra in palavra_secreta:
            if palpite == letra:
                letras_acertadas[index] = letra
            index += 1
        else:
            tentativas -= 1
            print(f"Vôce tem {tentativas} restantes")
            
            print(" ".join(letras_acertadas))
            
    if "_" not in letras_acertadas:
        print("Parabéns você ganhou!!")
    else:
        print(f"Você perdeu janjolão, a palavra era {palavra_secreta}")

    jogos.escolha_jogos()
  
if(__name__ == "__main__"):
    jogar()
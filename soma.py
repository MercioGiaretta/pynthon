nome = input("Digitai-vos vosso nome, por gentileza");
try:
    idade = int(input("Digitai-vos vossa idade, por gentileza"));
#idade = int;
except ValueError:
    print("Você não digitouum numero valído");
    print(f"Olá {nome}, você possui {idade} anos.");
    
try:
    n1 = float(input("Digite um número"));
    n2 = float(input("Digite mais um número"));
except ValueError:
    print("Tente novamente");
    
soma = n1 + n2

print (f"O número {n1} mais o número {n2} é igual a: {soma}.");
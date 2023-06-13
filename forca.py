from funcoes import limpa, perdeu, ganhou, menu
import os
limpa()
menu()

nome = input("Competidor digite seu nome: ")
desafiante = input("Desafiante digite seu nome: ")
limpa()
print('''
    Competidor nao olhe a Palavra hein...
''')
os.system('pause')
palavra = input("\nDigite a palavra secreta:").lower().strip()
dica1 = input("\nDigite a 1° dica: ")
dica2 = input("\nDigite a 2° dica: ")
dica3 = input("\nDigite a 3° dica: ")

for x in range(10):
    print()
digitadas = []
acertos = []
erros = 0

print("Bem vindo",nome)
print("""
                Digite (1) (2) e (3) para receber as dicas
X==:==
X  :
X  O
X \|/           Vc tem 5 vidas Tome Cuidado!
X / \ 
X
===========
A quantidade de letras são:
""")

while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else "_ "
    print(senha)    
    if senha == palavra:
        ganhou()
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa == "1":
        print("\nA 1° dica é ->",dica1)
    elif tentativa == "2":
        print("\nA 2° dica é ->",dica2)
    elif tentativa == "3":
        print("\nA 3° dica é ->",dica3)    
    try:
        digitadas
    except:
        print("Caracter inválido")
        continue

    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")

    print("X==:==\nX  :   ") 
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 5:
        print("Enforcado!")
        perdeu()
        break
#Adicionando logs
logs = open("Logs.txt","w")
logs.write("A Palavra: %s \n" % palavra)
if erros == 5:
    print("O Desafiante Ganhou!")
    logs.write("O Desafiante Ganhou!")
else:
    print("O Desafiado Ganhou!")
    logs.write("O Desafiado Ganhou!")
logs.close()
os.system('pause')


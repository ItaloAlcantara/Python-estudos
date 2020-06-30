import random




def jogar():

    bem_vindo()

    palavra_secreta_arq = le_arquivo_texto()

    numero_aleatorio = random.randrange(0, len(palavra_secreta_arq))

    palavra_secreta = palavra_secreta_arq[numero_aleatorio]

    letras_acertadas = mascar_palavra_secreta(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    chances = 1


    ##Enquento true and true permanece no loop
    while(not enforcou and not acertou):
        chute = solicita_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            print('Ainda faltam acertar {} letras'.format(str(letras_acertadas.count('_'))))
            print("Voce usou {} de 5 chances".format(chances))
            chances += 1

        print(letras_acertadas)
        acertou = "_" not in letras_acertadas
        enforcou = chances == 6

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")


    print("Fim do jogo.")



def bem_vindo():
    print("*************************")
    print("Bem vindo ao Jogo********")
    print("*************************")

def le_arquivo_texto():
    palavra_secreta_arq = []
    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavra_secreta_arq.append(linha.strip().lower())
    return palavra_secreta_arq

def mascar_palavra_secreta(palavra_secreta):
    # Para cada letra dentro da palavra secreta colocar o X (LIST COMPREHENSION)
    # USANDO IF EM LIST COMPREHENSION
    # pares = [x for x in inteiros if x % 2 == 0]
    # Jeito não limpo de se fazer a mesma coisa de cima
    # letras_feias = []
    # for letr in palavra_secreta:
    #     letras_feias.append("X")
    return ["_" for letra in palavra_secreta]

def solicita_chute():
    return input("Qual letra?").lower().strip()

def marca_chute_correto(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:

        if (chute.lower() == letra.lower()):
            letras_acertadas[index] = chute
        index += 1
if(__name__ == "__main__"):
    jogar()

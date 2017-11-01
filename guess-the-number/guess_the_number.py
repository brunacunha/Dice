from random import randint

# Declarando inicialmente os valores globais
MAX_NUMBER = 100
TENTATIVAS = 5
NUMERO_SORTEADO = randint(0, MAX_NUMBER)

# Função criada inicialmente para evitar código boilerplate
def quantas_tentativas(numero):
    print("Voce tem %i tentativas" %numero)

while True:
    resposta_usuario = int(input("Digite o seu numero de 0 a %i: " %MAX_NUMBER))
    if resposta_usuario > NUMERO_SORTEADO:
        TENTATIVAS -= 1
        print("O seu numero é maior, tente de novo")
        quantas_tentativas(TENTATIVAS)
    elif resposta_usuario < NUMERO_SORTEADO:
        TENTATIVAS -= 1
        print("O seu numero é menor, tente de novo")
        quantas_tentativas(TENTATIVAS)
    elif resposta_usuario == NUMERO_SORTEADO:
        print("Parabéns! Você acertou! :D")
        break
    if TENTATIVAS == 0:
        print ("Suas chances acabaram. :(")
        print("O número era %i" %NUMERO_SORTEADO)
        break

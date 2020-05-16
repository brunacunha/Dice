import random

while True:
    print('-=-='*10)
    print(random.randint(1,6))
    while True:
        resp = str(input('Deseja continuar? [S / N] ')).upper()
        if resp in 'SN':
            break
        else:
            print('[\033[1;31mERROR\033[m] Código não pode ser aceito, tente de novo')
    if resp == 'N':
        break

import random
numero_secreto = random.randint(1,150)
tentativas = 5

print('==== VOCÊ TEM 5 TENTATIVAS ====')
while tentativas > 0:
    chute = int(input('chute um número entre 1 e 150: '))

    if chute == numero_secreto:
        print('Parabéns, voce acertou!')
        break

    if chute > numero_secreto:
        print ('NÚMERO SECRETO É MENOR')
    else:
        print('NÚMERO SECRETO É MAIOR')

    tentativas = tentativas - 1
    print(f'você tem {tentativas} tentativas')
else:
    print('GAME OVER')
    print(f'O NÚMERO SECRETO É: {numero_secreto}')
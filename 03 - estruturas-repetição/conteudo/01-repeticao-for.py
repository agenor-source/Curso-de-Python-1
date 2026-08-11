# # Forma errada de repetir algo
# n1 = 1
# n2 = 2
# n3 = 3
# n4 = 4
# n5 = 5

# print(n1)
# print(n2)
# print(n3)
# print(n4)
# print(n5)

# #Forma certa de repetir algo => FOR
# print('====== REPETIÇÃO COM FOR ======')

# for i in range(5):
#     print(f'Numero: {i}')

# print(' === Contar até 50 de 2 em 2 =======')

# for i in range(1,50,2):
#     print(f'Número {i}')

# print('==== Perguntar várias vezes algo ====')

# qtd_pessoas = int(input('Quantas pessoas você quer cadastrar? '))
# for i in range(qtd_pessoas):
#     nome = input('Qual o seu nome? ')
#     print(f'Olá {nome}')

# # Exemplo - Tabuada do 9
# for i in range(1,11):
#     print(i * 9)

#     # start, stop, step
#     # Pergunte ao ususário a tabuada de um número e até quanto ele quiser
# tabuada = int(input('Qual a tabuada desejada? '))
# quantidade = int(input('Até quanto? '))
# for i in range(1, quantidade):
#     resultado = (quantidade * tabuada)
#     print(i * tabuada + 1)


#    # Crie um programa para escrever a seguinte letra de música:
# # 1 elefante incomoda muita gente
# # 2 elefantes incomodam muito mais
# print('1 Elefante incomoda muita gente')
# for i in range(2,11):
#     print(f'{i} Elefantes incomodam muito mais')

#    # Crie um programa para escrever a seguinte letra de música:
# # 1 elefante incomoda muita gente
# # 2 elefantes incomodam muito mais

# print()
# for i in range(1,11):
       
#     if i == 1:
#         print(f'{i} elefante incomoda muita gente')
#         print()
#     else:
#         print(f'{i} elefantes incomodam muita mais')
#         print()

# Pergunre ao usuário 5 números e diga se o número é positivo ou negativo
# for i in range(5):
#     numero = int(input('digite um número '))

#     if numero < 0 :
#         print(f'número negativo')
# else:
#         print('numero positivo')


# Pergunre ao usuário 5 números e diga se o número é positivo ou negativo
for i in range(5):
    numero = int(input('digite um número: '))

    if numero < 0 :
        print(f'número negativo.')
    elif numero > 0 :
        print('numero positivo.')
    else:
        print('não é positivo, nem negativo.')


print('Programa encerrado.')

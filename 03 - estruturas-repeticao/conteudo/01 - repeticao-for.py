# # Forma ERRADA DE REPETIR ALGO
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

# # Forma CERTA DE REPETIR ALGO FOR
# print('====== REPETICAO COM FOR ======')

# for i in range(5):
#     print(f'Numero: {i}')

# print('=== Contar ate 50 de 2 em 2 ===')

# for i in range(1,50,2):
#     print(f'Numero {i}')

# print('=== Perguntar varias vezes algo ===')

# qtd_pessoas = int(input('Quantas pessoas voce quer cadastrar? '))
# for i in range(5):
#     nome = input('Qual o seu nome? ')
#     print(f'Ola {nome}')

# Exemplo - Tabuada do 9
# Pensar na contagem 
# for i in range(11):
#     resultado = i * 9
#     print(f'{i} x 9 = {resultado}')

# Pergunte ao usuario a tabuada de um numero e ate quanto ele quer
numero = int(input('Deseja a tabuda de qual numero? '))
vezes = int(input('Deseja ir ate quanto? '))

for i in range(vezes+1):
    multiplicacao = i * numero
    print(f'{i} x {numero} = {multiplicacao}')
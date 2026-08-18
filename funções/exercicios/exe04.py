# crie um progrma que tenha uma função SuperSomador() que vai receber uma lista de números e retorna a soma de todos os números da lista. Pergunte ao usuário quantos números ele deseja somar, depois peça para ele digitar cada número e armazene-os em uma lista. Por fim, utilize a função SuperSomador() para receber dois
# numeros como parâmetros e depois vai retornar a soma de todos os valores no
# intervalo entre os valores recebidos
#Ex: 
# SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
# SuperSomador(15, 19) vai somar  15 + 16 + 17 + 18 + 19 e vai retornar 85

def SuperSomador(a, b):
    soma = 0

    for i in range(a, b + 1):
        soma += i
    return soma

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [15, 16, 17, 18, 19]

print(SuperSomador(1, 6))
print(SuperSomador(15, 19))

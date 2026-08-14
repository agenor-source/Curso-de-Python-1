# Pedir ao usuário dois números e com esses números
# calcular a soma, subtração, divisão, multiplicação
# e também pedir ao usuário um nome para saudá-lo

Numero  = int(input('digite um número: ')) 
Numero2 = int(input('digite outro número: '))

def soma(a, b):
    return a + b
print(f'A soma dos números é: {soma(Numero, Numero2)}')

def subtracao(a, b):
    return a - b
print(f'A subtração dos números é: {subtracao(Numero, Numero2)}')

def divisao(a, b):
    return a / b
print(f'A divisão dos números é: {divisao(Numero, Numero2)}')

def multiplicacao(a, b):
    return a * b
print(f'A multiplicação dos números é: {multiplicacao(Numero, Numero2)}')

nome = input('digite seu nome: ')

def saudacao(nome):
    return f"Olá, seja bem-vindo(a) {nome}"

mensagem = saudacao(nome)
print(mensagem)
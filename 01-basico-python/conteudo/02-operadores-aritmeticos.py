# OPERACOES ARITMETICAS
numero1 = 10
numero2 = 2

soma = numero1 + numero2
subtracao = numero1 - numero2
divisao_exata = numero1 / numero2
potencia = numero1 ** numero2
divisao_arredondada = numero1 // numero2
multiplicacao = numero1 * numero2
resto_divisao = numero1 % numero2

# print("A soma de", numero1, " + ", numero2, " = ", soma)
# print('A subtracao de', numero1, " - ", numero2, ' = ', subtracao)
# print('A divisao exata de',numero1, " / ", numero2, ' = ', divisao_exata)
# print('A potencia de', numero1, ' ** ', numero2, ' = ', potencia)
# print('A divisao arredondada de', numero1, ' // ', numero2, ' = ', divisao_arredondada)
# print('A multiplicao de', numero1, ' x ', numero2, ' = ', multiplicacao)
# print('O resto da divisao de', numero1, ' % ', numero2, ' = ', resto_divisao)

# Perguntando algo ao usuario input()
# Convertendo o valor do input para float ou int
# nota1 = float(input('Digite sua primeira nota: '))
# nota2 = float(input('Digite sua segunda nota: '))
# media = 0.0

# media = (nota1 + nota2) / 2

# print('A media do aluno é', media)

#pergunte ao usario o nome, idade, altura e mostre o print final (frase)
nome = input("Qual seu nome? ")
idade = int(input('Qual sua idade? '))
altura = float(input('Qual a sua altura: '))

# print("Ola seja bem-vindo(a)",nome, 'voce tem', idade, 'anos', 'e tem', altura, 'm')

# Perguntar o o usario peso, altura e no final mostrar o IMC
nome = input('Qual o seu nome? ')
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso / altura ** 2

print('Ola, seja bem-vindo', nome, 'seu IMC é de', round(imc,2))

# Crie um programa que solicite o peso e altura e mostre o imc da pessoa 
nome = (input('Nome: '))
peso = float(input('Peso: '))
altura = float(input( 'Altura: '))
imc = peso / altura ** 2 
imc_resumido = round(imc,2)


if imc < 18.5 :
    print(nome, 'está abaixo do peso')
elif  imc >= 18.5 and imc <= 24.9:
    print(f'Ola, prazer {nome} - Seu imc é {imc_resumido} está no peso regular')
elif imc >= 25 and imc <= 29.9:
    print(f'Ola, prazer {nome} - Seu imc é {imc_resumido} está em excesso de peso')
elif imc >=30 and imc <= 34.9:
    print(f'Ola, prazer {nome} - Seu imc é {imc_resumido} está em obesidade grau I')
elif imc >=35 and imc <= 39.9:
    print(f'Ola, prazer {nome} - Seu imc é {imc_resumido} está em obesidade grau II')
else:
    print(f'Ola, prazer {nome} - Seu imc é {imc_resumido} está em obesidade grau III')

# Comparação de idade
# Crie um programa que receba uma idade e realize comparações utilizando
# operadores relacionais
idade = int(input('Digite sua idade: '))

idade_maior_igual_18 = idade >= 18
menor_idade = idade < 18
idade_igual_20 = idade == 20

print('---------------------------')
print(f'A pessoa possui 18 anos ou mais: {idade_maior_igual_18}')
print(f'A pessoa é menor de idade: {menor_idade}')
print(f'A idade é igual a 20 anos: {idade_igual_20}')
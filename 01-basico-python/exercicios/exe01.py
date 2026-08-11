# Cadastro de usuário
# Crie um programa que solicite informações de uma pessoa e depois exiba
# todos os dados cadastrados.

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Digite sua cidade: ')
altura = float(input('Digite sua altura: '))
carteira = input('Possui carteira de motorista? (S/N) ')
possui_carteira = carteira == 'S' or carteira == 's'

print('--- Dados do Usuário ---')

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Cidade: {cidade}')
print(f'Altura: {altura}')
print(f'Possui carteira de motorista: {possui_carteira}')
# Validação de acesso
# Um sistema precisa verificar duas informações:
# Se o usuário possui cadastro.
# Se a senha está correta.
# Crie um programa que receba essas informações e utilize o operador lógico 
# AND 

cadastro = input('Usuario possui cadastro? (S/N) ')
senha = input('Senha está correta: (S/N) ')
validacao =  (cadastro == 'S' or cadastro == 's') and (senha == 'S' or senha == 's')

print('-----------------------------')

print(f'Resultado da validação: {validacao}')
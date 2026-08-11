#  Inversão de valor com NOT
# Um sistema precisa verificar o estado de uma conta.
# Utilize o operador 
# NOT
#  para inverter o valor recebido
conta = input('A conta esta bloqueada: (S/N)')
conta_bloqueada = not conta == 'S' and conta == 's'
print(f'A conta esta liberada: {conta_bloqueada}')
 # Caixa Eletrônico

saldo = 500

while saldo > 0:
    print(f'Saldo atual: R$ {saldo}')
    saque = float(input('Digite o valor que deseja sacar (0 para encerrar):'))
    if saque == 0:
        print('Atendimento encerrado pelo usuário.')
        break
    if saque > saldo:
        print ('Erro: Saldo insuficiente para este saque')
        continue
    saldo -= saque
    print (f'Saque realizado com sucesso. Saldo restante: R$ {saldo}')
else:
    print('Saldo zerado. Não é possivel realizar mais saques.')

    


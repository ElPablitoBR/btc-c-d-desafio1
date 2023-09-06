import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
total_saque_diario = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = input('Valor do depósito (número inteiro e positivo): ')

        if valor.isdigit() and int(valor) > 0:
            valor = int(valor)
            saldo += valor
            data_hora = datetime.datetime.now()
            extrato.append(('d', valor, data_hora))
            print('Depósito realizado com sucesso.')
        else:
            print(
                'Valor de depósito inválido. O valor deve ser um número inteiro positivo.')
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print('Quantidade de saques diários atingido.')
        else:
            try:
                valor = int(input('Valor do saque: '))
                if valor > 0 and total_saque_diario + valor <= limite:
                    if valor > saldo + limite:
                        print('Saldo insuficiente.')
                    else:
                        saldo -= valor
                        data_hora = datetime.datetime.now()
                        extrato.append(('s', valor, data_hora))
                        numero_saques += 1
                        total_saque_diario = total_saque_diario + valor
                        print('Saque realizado com sucesso.')
                else:
                    print('Valor limite de saque diário atingido.')
            except ValueError:
                print('O valor do saque deve ser um número inteiro positivo.')
    elif opcao == 'e':
        print('\nExtrato Bancário')
        print('#####################################################\n')
        print('| OP | Data/Hora           | Valor')
        print('-----------------------------------------------------')
        for operacao, valor, data_hora in extrato:
            if operacao == 'd':
                print(
                    f'| D  | {data_hora.strftime("%d-%m-%Y %H:%M:%S")} | R${valor}')
            elif operacao == 's':
                print(
                    f'| S  | {data_hora.strftime("%d-%m-%Y %H:%M:%S")} |-R${valor}')
        print('-----------------------------------------------------')
        print('#####################################################')
        print(
            f'| Saldo em {data_hora.strftime("%d-%m-%Y %H:%M:%S")} -> R$ {saldo}')

        print('#####################################################\n')
    elif opcao == 'q':
        print('Você saiu do sistema...')
        break
    else:
        print('Opção inválida.')

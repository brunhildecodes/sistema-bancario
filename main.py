from objetos.sistema import Sistema

escolha = True
s = Sistema()

print('Olá, Seja bem-vindo de volta!\nVamos iniciar o expediente de hoje.\n')
while escolha != False:
    print('\nMenu:\n1 - Cadastrar cliente\n2 - Realizar atendimento\n3 - Visualizar fila atual\n4 - Visualizar o histórico de atendimento\n5 - Encerrar expediente\n6 - Desfazer último atendimento.')
    escolha = input('\nQuais das opções você deseja realizar agora: ')
    match escolha:
        case '1':
            print('')
            print('Preciso de algumas informações pra cadastrar este cliente:')
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            print('Serviços disponíveis:\n1 - Abrir conta\n2 - Fechar conta\n3 - Pagamento\n4 - Deposito\n5 - Saque')
            servico = int(input('Serviço: '))
            print('Tipos de atendimento:\nPrioritário: P01\nComum: C02')
            prioridade = input('Tipo de atendimento: ')
            cliente = {
                'nome': nome,
                'idade': idade,
                'servico': servico,
                'p': prioridade
            }
            print(s.cadastrar_cliente(cliente))
        case '2':
            print('')
            print(s.iniciar_atendimento())
        case '3':
            print('')
            print(f'Quantidade de clientes na fila: {s.fila_atual()}')
        case '4':
            print('')
            s.historico_atendimento()
        case '5':
            print('')
            if s.fila_atual() > 0:
                print(f'Não é possível finalizar o expediente, ainda há {s.fila_atual()} clientes para atendimento:')
            else:
                print('Expediente finalizado com sucesso!\nHistórico de atendimento:')
                s.historico_atendimento()
                escolha = False
        case '6':
            print('')
            if s.historico.esta_vazia():
                print('Ainda não houve atendimentos neste expediente.')
            else:
                # se o cliente desejar realizar algum outro atendimento, pergunta o serviço desejado
                opcao = input('O cliente deseja realizar outro atendimento? ')
                if opcao.lower() == 'sim':
                    servico = int(input('Digite o número do serviço desejado: '))
                    s.desfazer_ultimo_atendimento(opcao, servico=servico)
    
                # caso não, apenas desfaz o atendimento
                else:
                    print(s.desfazer_ultimo_atendimento(opcao))

        # se o usuario digitar uma opção que não esteja no menu        
        case _:
            print('Opção inválida, tente uma dessas:')

    


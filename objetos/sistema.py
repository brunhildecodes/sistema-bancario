from estruturas.fila import Fila
from estruturas.pilha import Pilha

class Sistema:
    def __init__(self):
        self.fila = Fila()
        self.fila_prioritaria = Fila()
        self.tamanho = 0
        self.historico = Pilha()
        self.cancelamentos = 0
        # definir os atendimentos dos clientes por aqui:

# esse já ta OK
# vai receber um dicionario com nome, idade e serviço
    def cadastrar_cliente(self, cliente): 
        if cliente['p'].lower() == 'p01':
            self.fila_prioritaria.enfileira(cliente)
            self.tamanho += 1
            return 'Cliente cadastrado com sucesso!'
        elif cliente['p'].lower() == 'c02':
            self.fila.enfileira(cliente)
            self.tamanho += 1
            return 'Cliente cadastrado com sucesso!'
        else:
            return 'Não foi possível realizar o cadastro.\nTente P01 para atendimento prioritário ou C02 para atendimento comum.'

# esse já ta OK
    def historico_atendimento(self):
        p = 0 # prioridade
        c = 0 # comum
        s1 = 0 # abrir conta
        s2 = 0 # fechar conta
        s3 = 0 # pagamento
        s4 = 0 # deposito
        s5 = 0 # saque
        for i in self.historico.items:
            if i['p'].lower() == 'p01':
                p += 1
            else:
                c += 1
        for i in self.historico.items:
            if i['servico'] == 1:
                s1 += 1
            elif i['servico'] == 2:
                s2 += 1
            elif i['servico'] == 3:
                s3 += 1
            elif i['servico'] == 4:
                s4 += 1
            elif i['servico'] == 5:
                s5 += 1
            elif i['servico'] == 0:
                s6 +=1
        print(f'Total de atendimentos: {len(self.historico.items)}')
        print(f'Total de atendimentos prioritários: {p}')
        print(f'Total de atendimentos comuns: {c}')
        print(f'Total de atendimentos cancelados: {self.cancelamentos}')
        print(f'Serviços realizados:')
        print(f'Abrir conta: {s1} \nFechar conta: {s2}\nPagamento: {s3}\nDeposito: {s4}\nSaque: {s5}')

# esse já ta OK
# para cada um cliente prioritario atendido -> atender um comum
    def iniciar_atendimento(self):
        if self.historico.items:
            anterior = self.historico.topo()['p'].lower()
        else:
            anterior = None
        if self.tamanho > 0: # verifica se existe clientes para atendimento
            if self.fila_prioritaria.tamanho() != 0 and (anterior != 'p01' or self.fila.tamanho() == 0): # verifica se existe algum cliente prioritario e se o cliente anterior n foi prioritario ele vai atender um.
                atendimento = self.fila_prioritaria.desinfileira()
                if atendimento:
                    self.historico.push(atendimento)
                    self.tamanho -= 1
                    return 'Você realizou um atendimento prioritário.'
            elif self.fila.tamanho() != 0 and (anterior != 'c02' or self.fila_prioritaria.tamanho() == 0):
                atendimento = self.fila.desinfileira() # caso não haja nenhum cliente prioritario e o anterior n tiver sido comum, vai realizar um atendimento comum
                if atendimento:
                    self.historico.push(atendimento)
                    self.tamanho -= 1
                    return 'Você realizou um atendimento comum.'
        # caso n tenha clientes na lista
        return 'Não há clientes para este expediente.'

    def fila_atual(self):
        return self.tamanho
    
    def desfazer_ultimo_atendimento(self, escolha, servico = None):
        if self.historico:
            cliente = self.historico.pop()
            if escolha.lower() == 'sim':
                if servico:
                    cliente['sevico'] = servico
                self.cadastrar_cliente(cliente)
                return 'Cliente de volta na fila.'
            else:
               self.cancelamentos += 1
            return 'Atendimento desfeito com sucesso!'
        else:
            None
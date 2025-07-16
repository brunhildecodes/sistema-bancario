
# Projeto de Estrutura de Dados: Sistema de Atendimento Bancário.

 O projeto propõe uma simulação de atendimento bancário, organizando os clientes em duas filas: uma prioritária e uma comum. A ideia é que, para cada cliente prioritário atendido, um comum também seja atendido, mantendo um atendimento mais equilibrado entre os dois tipos.


## Funcionalidades

- Cadastrar clientes

    ``Armazena dicionários com informações dos clientes (nome, idade, serviço e prioridade) nas filas de acordo com o tipo de atendimento.``
- Fila atual

    ``Retorna o total de clientes para atendimento.``
- Historico de atendimento

    ``Imprime o total de atendimentos e as quantidades de atendimentos por tipo de serviço.``
- Desfazer atendimento

    ``desfaz o último atendimento e caso o cliente queira fazer outro tipo de serviço retorna ele pra fila com o serviço desejado.``
- Realizar atendimento

    ``Atende os clientes de acordo com a prioridade, começando por um prioritário e depois um comum.``

## Estruturas usadas:

- Fila

    `` Usei filas para cadastrar os clientes no sistema. Dividi o atendimento em uma fila comum e uma fila prioritária, permitindo organizar melhor os tipos de cliente e controlar a ordem dos atendimentos.``
- Pilha

    `` A pilha foi usada para registrar o histórico dos atendimentos, foi útil para acompanhar o tipo de cliente atendido anteriormente, o que ajudou a equilibrar o atendimento entre prioritários e comuns e para o método de desfazer atendimentos.``
- Dicionário

    ``Os clientes foram representados como dicionários, pois o formato chave-valor facilitou o acesso e a organização das informações, como nome, idade, serviço e tipo de atendimento.``



## Rodando localmente
É necessário ter o python 3.10 instalado.

Clone o projeto

```bash
  git clone https://github.com/brunhildecodes/sistema-bancario.git
```
Execute no terminal
```bash
    python main.py
```


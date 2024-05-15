class Cadastro:

    def __init__(self,nome : str, CPF : str, idade: int):
        self.nome = nome
        self.cpf = CPF
        self.idade = idade
    
cliente_lista = []

for i in range(5):
    nome = input('Digite seu nome : ')
    cpf = input('Digite seu CPF: ')
    idade = int(input('Digite sua idade: '))

    cadastro = Cadastro(nome, cpf, idade)

    cliente_lista.append(cadastro) 
    
for clientes in cliente_lista:
    print(f'Clinte: ',cadastro.nome, 'CPF: ',cadastro.cpf, 'Idade: ',cadastro.idade)




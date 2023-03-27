# Para praticar, aqui estão alguns exercícios para você:
# Crie uma classe chamada ContaBancaria que tenha os seguintes atributos: saldo (um número float) e titular (uma string).
#
# Adicione um método chamado depositar que permita ao usuário depositar dinheiro na conta.
# Adicione um método chamado sacar que permita ao usuário sacar dinheiro da conta.
# Adicione um método chamado imprimir_saldo que imprima o saldo atual da conta.

# Crie um objeto da classe ContaBancaria e chame seus métodos para depositar e sacar dinheiro, e depois imprima o saldo atual da conta.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = str(titular)
        self.saldo = round(float(saldo), 2)

    def depositar_dinheiro(self):
        valor_deposito = float(input('Quanto você deseja depositar? Se desejar sair digite 0\n'))
        if valor_deposito == 0:
            pass
        else:
            self.saldo += valor_deposito
            print(f"Olá sr(a) {self.titular}, seu deposito foi realizado com sucesso! \nObrigado!\n \n \n")

    def sacar_dinheiro(self):
        valor_saque = float(input('Quanto você deseja depositar? \nSe desejar sair digite 0\n'))
        if valor_saque == 0:
            pass
        else:
            self.saldo -= valor_saque
            print("Olá sr(a) {}, seu saque foi realizado com sucesso! \nObrigado!\n \n \n" .format(self.titular))

    def imprimir_saldo(self):
        print(f'Seja muito bem vindo sr(a) {self.titular}, \n'
              f'o saldo atual da sua conta é R$ {round(self.saldo, 2)}\n \n \n')

#####################################################################
# Aqui seria feito um sistema login e senha para encontrar
# o usuario correto e puxar os dados do Banco de Dados

contas = {
    "8064": ContaBancaria("André", 500.00),
    "2055": ContaBancaria("Rafael", 250.00),
    "2711": ContaBancaria("Paola", 1500.00)
}
#####################################################################

while True:
    conta = input('Digite o numero da sua conta: ')
    if conta in contas:
        login = ContaBancaria
        break
    else:
        print('Erro, número de conta inválida!')

print('Olá {}! Seja bem vindo ao banco!\n'.format(contas[conta].titular))


while True:
    menu = int(input(f'Digite 1 - Para Deposito Bancário\n'
                     f'Digite 2 - Sacar Dinheiro\n'
                     f'Digite 3 para ver o saldo da sua conta\n'
                     f'Ou digite 0 para sair\n'))

    if menu == 1:
        contas[conta].depositar_dinheiro()
        menu == None

    elif menu == 2:
        contas[conta].sacar_dinheiro()
        menu == None

    elif menu == 3:
        contas[conta].imprimir_saldo()
        menu == None

    elif menu == 0:
        break

    elif menu > 0 or menu >= 4:
        print('Desculpe, essa opcao não existe, tente novamente!')
import openpyxl

#Carregar o arquivo
workbook = openpyxl.load_workbook('Database.xlsx')
sheet = workbook['Sheet']

#Pedir para o usuario digitar o usuario e a senha
usuario = input('Digite o usuario: ')
senha = input('Digite a senha: ')

#Procurar o usuario e senha na planilha
usuario_encontrado = False
senha_correta = False

#min_row=2 para começar da segunda linha e apenas valores verdadeiros
for row in sheet.iter_rows(min_row=2, values_only=True):
    if row[0] == usuario:
        usuario_encontrado = True
        if row[1] == senha:
            senha_correta = True
        break

#Verificar se o usuario e a senha estão corretas:

if usuario_encontrado and senha_correta:
    print('login bem sucedido')
else:
    print('Usuario ou senha incorretos')

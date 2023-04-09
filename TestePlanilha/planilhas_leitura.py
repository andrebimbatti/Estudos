import openpyxl

# Carregando um arquivo
book = openpyxl.load_workbook('Database.xlsx')
# Selecionando uma página
cadastro_db = book['Sheet']

#Imprimindo os dados de cada linha
linhas = list(book['Sheet'].rows)
print(linhas[0:])
print('#' * 50)

for rows in cadastro_db.iter_rows(min_row=2):
    #Para imprimir a linha toda em uma linha
    print(rows[0].value, rows[1].value)

    # Se for imprimir um por linha
    # for cell in rows:
    #     print(cell.value)
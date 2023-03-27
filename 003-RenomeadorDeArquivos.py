import os

# Solicita o nome base ao usuário
nome_base = input("Digite o nome base para os arquivos: ")

# Solicita o caminho da pasta ao usuário
caminho_pasta = input("Digite o caminho da pasta onde estão os arquivos: ")

# Obtém a lista de arquivos na pasta informada pelo usuário
arquivos = os.listdir(caminho_pasta)

# Define um contador para numerar os arquivos
contador = 1

# Percorre a lista de arquivos e renomeia cada um de acordo com o padrão informado
for arquivo in arquivos:
    # Obtém o caminho completo do arquivo
    caminho_arquivo_antigo = os.path.join(caminho_pasta, arquivo)

    # Obtém a extensão do arquivo
    nome_arquivo, extensao = os.path.splitext(arquivo)

    # Define o novo nome para o arquivo
    novo_nome = f"{nome_base}_{contador:03d}{extensao}"

    # Obtém o caminho completo do novo arquivo
    caminho_arquivo_novo = os.path.join(caminho_pasta, novo_nome)

    # Renomeia o arquivo
    os.rename(caminho_arquivo_antigo, caminho_arquivo_novo)

    # Incrementa o contador
    contador += 1

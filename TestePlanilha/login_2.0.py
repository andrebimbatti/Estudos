#coding: utf-8
#author: Andre Luiz Bimbatti Assumpcao Junior


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window #modulo que controla as propriedades da janela
from kivy.utils import get_color_from_hex #modulo que permite vc colocar as cores por codigo hexadecimal
import openpyxl

# Carregando o arquivo dabase.xlsx
workbook = openpyxl.load_workbook('Database.xlsx')
sheet = workbook['Sheet']

# Definindo a cor da janela para branco em hex decimal
# através da função importada get_color_from_hex

Window.clearcolor = get_color_from_hex("#FFFFFF")

#definindo o tamanho da tela
Window.size = (500, 170)

janela = None

class Tela(GridLayout):
    def login(self):
        #imprime o usuario e senha digitados quando o botao é pressionado
        print(self.ids.user.text, self.ids.senha.text)
        
        #Passando para a variavel o usuario e senha digitados
        usuario = str(self.ids.user.text)
        senha = str(self.ids.senha.text)

        usuario_encontrado = False
        senha_correta = False

        #checando o usuario e senha na database xlsx
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[0] == usuario:
                usuario_encontrado = True
                if row[1] == senha:
                    senha_correta = True
                break
        
        #Verificar se acertou o usuario e a senha correta:
        if usuario_encontrado and senha_correta:
            print('login bem sucedido')
        else:
            print('Usuario ou senha inválidos')
        




        

    pass

class JanelaApp(App):
    def build(self):
        return

janela = JanelaApp()
janela.run()




#######################################CODIGO FUNCAO#######################################





###########################################################################################
import math
from rich import print

peso = float(input('Digite seu peso em KGs ex.: 80.00 \n'))
altura = float(input('Digite sua altura e centimetro, ex.: 1.70 \n'))

def calcular_imc():
    calculo_imc = round(peso / (altura * altura), 2)

    if calculo_imc < 18.5: #Magreza
        print("Seu IMC é igual a: \n" + str(calculo_imc) + "\n[green]Você está no indice de Magreza[/]")
    
    elif calculo_imc > 18.5 and calculo_imc <= 24.9: #Peso Normal
        print("Seu IMC é igual a: \n" + str(calculo_imc) + "\n[green]Você está com o peso Normal[/]")

    elif calculo_imc > 25 and calculo_imc <= 29.9: #Sobrepeso
        print("Seu IMC é igual a: \n" + str(calculo_imc) + "\nVocê está com Sobrepeso[/]")

    elif calculo_imc > 30 and calculo_imc <= 34.9: #Obesidade Grau I
        print("Seu IMC é igual a: \n" + str(calculo_imc) + "\n[red]Você está com Obesidade Grau I[/]")

    elif calculo_imc > 35 and calculo_imc <= 40: #Obesidade Grau II
        print("Seu IMC é igual a: \n" + str(calculo_imc) + "\n[red]Você está com Obesidade Grau I[/]")

    elif calculo_imc > 40: #Obesidade Grau III
        print("Seu IMC é igual a: \n" + str(calculo_imc) + "\n[red]Você está com Obesidade Grau I[/]")



calcular_imc()

# def soma(x,y):
#     total = x + y
#     print('O total da soma dos números é: ', total)

# a = input('Digite um numero: ')
# b = input('Digite outro numero: ')

# soma(int(a), int(b))


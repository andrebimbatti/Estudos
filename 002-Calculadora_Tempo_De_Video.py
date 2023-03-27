#coding: Utf-8

#author: ANDRE LUIZ BIMBATTI ASSUMPCAO JUNIOR

def calcular_tempo_de_video():
    tamanho_do_video = float(input('Digite o tempo de duração do vídeo em minutos: '))
    velocidade = float(input('Digite a velocidade que vai ser assistido o vídeo: '))
    duracao = int((tamanho_do_video / velocidade))
    horas = duracao // 60
    minutos = duracao % 60
    print('O vídeo terá a duração de {}h{}m ou {} minutos'.format(horas, minutos, duracao))

calcular_tempo_de_video()


lista_musicos = [ 'Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal',\
                 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa'] 
import time
import random

def jogo_numero():
  jogo = True
  while jogo:

    print("Bem vindo ao jogo do numero secreto")
    print("A pool de numeros contem 16 opcoes, e cada uma e um cantor diferente ")
    print("Escolha 3 numeros entre 0 e 15 : ")
    print("Obs -> Se nao escolher corretamente ,exibiremos os numeros 3, 9 e 14 e um numero randomizado")
    
    escolha1 = int(input("Digite o primeiro numero : "))
    time.sleep(1)
    escolha2 = int(input("Digite o segundo numero: "))
    time.sleep(1)
    escolha3 = int(input("Digite o terceiro numero :"))


    if (escolha1 < 0 or escolha1 > 15) or (escolha2 < 0 or escolha2 > 15) or (escolha3 < 0 or escolha3 > 15):
      for i in range(len(lista_musicos)):
        print("Musico 1 :", lista_musicos[i][3], ", Musico 2 : ", lista_musicos[i][9], ", Musico 3 : ", lista_musicos[i][14])
        continue

    elif:
      print(f'Musico1: {lista_musicos[escolha1]}, Musico2: {lista_musicos[escolha2]},Musico3: {lista_musicos[esoclha3]}')
      jogo = False

jogo_numero()

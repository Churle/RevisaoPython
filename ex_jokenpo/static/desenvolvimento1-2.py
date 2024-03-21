import time
import random

lista_musicos = ['Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal',
                 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa']

def jogo_numero():
    jogo = True
    while jogo:
        print("Bem vindo ao jogo do numero secreto")
        print("A pool de numeros contem 16 opcoes, e cada uma e um cantor diferente ")
        print("Escolha 3 numeros entre 0 e 15 : ")
        print("Obs -> Se nao escolher corretamente, exibiremos os números 3, 9 e 14 e um número randomizado")
        print()
        print(lista_musicos)
        print()

        escolha1 = int(input("Digite o primeiro numero : "))
        time.sleep(1)
        escolha2 = int(input("Digite o segundo numero: "))
        time.sleep(1)
        escolha3 = int(input("Digite o terceiro numero :"))

        # Validação das escolhas
        if (escolha1 < 0 or escolha1 >= len(lista_musicos)) or \
           (escolha2 < 0 or escolha2 >= len(lista_musicos)) or \
           (escolha3 < 0 or escolha3 >= len(lista_musicos)):
            print("Escolha inválida! As escolhas devem estar entre 0 e 15.")
            print("Músico 1 :", lista_musicos[3])
            print("Músico 2 :", lista_musicos[9])
            print("Músico 3 :", lista_musicos[14])
            print()
            
            # Chamando o número aleatório
            aleatorio = random.choice(lista_musicos)
            print(f'A escolha aleatória é {aleatorio}')
            print()
            continue

        # Escolhas corretas
        else:
            print(f'Musico1: {lista_musicos[escolha1]}, Musico2: {lista_musicos[escolha2]}, Musico3: {lista_musicos[escolha3]}')
            jogo = False

jogo_numero()

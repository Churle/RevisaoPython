import random
from time import sleep 
import colorama
from colorama import Fore  # Correção aqui: 'Fore' em vez de 'fore'

# Inicializar o colorama
colorama.init()

jokenpo = ["pedra", "papel", "tesoura"]

def jokengame():
    jogo = True
    while jogo:
        print("Jogador 1 escolher entre: pedra, papel, tesoura ou 'sair' para cancelar o jogo")
        jogador1 = input("Jogador 1: ").lower()
        if jogador1 == 'sair':
            print("Jogo encerrado.")
            break
        elif jogador1 not in jokenpo:
            print("Escolha inválida. Tente novamente.")
            continue

        print("Aguardando jogador 2...")
        sleep(3)  # Aguarda 3 segundos antes da escolha do jogador 2

        jogador2 = random.choice(jokenpo)
        print("Jogador 2 escolheu:", jogador2)

        if jogador1 == jogador2:
            print(Fore.BLUE + "Empate. Tentem novamente.")
        elif (jogador1 == 'pedra' and jogador2 == 'tesoura') or \
             (jogador1 == 'tesoura' and jogador2 == 'papel') or \
             (jogador1 == 'papel' and jogador2 == 'pedra'):
            print(Fore.GREEN + "Jogador 1 Venceu, pois", jogador1, "ganha de", jogador2)
            jogo = False
        else:
            print(Fore.RED + "Jogador 2 Venceu, pois", jogador2, "ganha de", jogador1)
            jogo = False

jokengame()

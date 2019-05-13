from random import randint  # Importa a função de gerar números aleatórios

print("Olá 1info02!")

Dado1 = randint(1, 6)
print("dado1: ", Dado1)

Dado2 = randint(1, 6)
print("dado2: ", Dado2)

Dado3 = randint(1, 6)
print("dado3: ", Dado3)

Dado4 = randint(1, 6)
print("dado4: ", Dado4)

jogador1 = Dado1 + Dado2
jogador2 = Dado3 + Dado4

print('jogador1:', jogador2)
print('jogador2:', jogador1)

if jogador1 > jogador2:
    print("Jogador1 venceu!")
else:
    if jogador2 > jogador1:
        print("jogador 2 venceu")
    else:
        print("empate!")

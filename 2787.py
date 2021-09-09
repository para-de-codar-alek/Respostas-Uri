# Saber a cor da casa inferior direita de um meio tabuleiro de xadez de n linha e colunas
# Sabendo q a primeira casa é sempte branca
# Se o tabuleiro tiver linhas pares e colunas ímpares, logo vai ser preta
# se tiver coluna par e linha impar tmb
L = int(input())
C = int(input())

if L % 2 == 0  and C % 2 != 0 or C % 2 == 0 and L % 2 !=0:
    print (0)
else:
    print(1) 
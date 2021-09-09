#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
# caso haja uma divisão por 0 ou raiz de numero negativo.
# A <-- value, B <-- Value, C <-- Value
# Import math
# Bhask recebe calculo do delta
# root recebe raiz do delta
# x recebe uma das raízes
# x2 a outra
# Se root <0 or a==0 ''Impossível de calcular''
line = input().split()
A, B, C = line
A = float(A)
B = float(B)
C = float(C)
if (A == 0 or B**2 - 4*A*C< 0):
    print('Impossivel calcular')
else:
    x1 = (-B + (B**2 - 4 * A * C)**(1/2))/(2 * A)
    x = (-B - (B**2 - 4 * A * C)**(1/2))/(2 * A)
    print ('R1 = {:.5f}'.format(x1))
    print ('R2 = {:.5f}'.format(x))
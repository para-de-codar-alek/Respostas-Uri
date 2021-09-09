# Programa das carinhas triste ou felizes, condições:
#Se a/ temperatura desceu do 1º para o 2º dia, mas subiu ou permaneceu constante do 2º para o 3º, felizes
#Se a/ temperatura subiu do 1º para o 2º dia, mas desceu ou permaneceu constante do 2º para o 3º, tristes
#Se a/ temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º menos do que subira do 1º para o 2º, tristes
#Se a/ temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º no mínimo o tanto que subira do 1º para o 2º,felizes
#Se a/ temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º menos do que descera do 1º para o 2º, felizes
#Se a/ temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º no mínimo o tanto que descera do 1º para o 2º, tristes
#Se a temperatura permaneceu constante do 1º para o 2º dia, as pessoas ficam felizes se subiu do 2º para o 3º dia ou tristes caso contrário (respectivamente, sétima e oitava figuras).
line = input().split()
A, B, C = line
A = int(A) 
B = int(B) 
C = int(C) 
if (A > B):
    if C > B:
        print (':)')
    else:
        if (B-C < A-B):
            print (':)')
        else:
            print (':(')


elif (A<B):
    if C<B:
        print (':(')
    else:
        if (B-C > A-B):
            print (':(')
        else:
            print (':)')

else:
    if C>A:
        print (':)')
    else:
        print (':(')



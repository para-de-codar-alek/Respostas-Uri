# Receber os lados do triângulo, dizer se ele existe dar o perímetro e senão dar à área do trapézio
# line <-- entrada
# a,b,c <-- line e flootando a, b e c
# se b-c<a e a<b+c ou a-c<b e b<a+c ou a-b<c e c<a+b
# pm = a+b+c
# senão
# area= ((a+b)*c)/2
line = input().split()
A, B, C = line
A = float(A)
B = float(B)
C = float(C)
if ((B-C) < A < (B+C) and (A-C) < B < (A+C) and (A-B) < C < (A+B)):
    Perimetro = A + B + C
    print('Perimetro = {:.1f}'.format(Perimetro))
else:
    Area = ((A+B)*C)/2
    print ('Area = {:.1f}'.format(Area))
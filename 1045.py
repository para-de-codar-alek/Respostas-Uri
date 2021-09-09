
linha = input().split()
linha = list(map(float,linha))
A, B, C = sorted(linha)[::-1]
if (A>=B+C):
    print ('NAO FORMA TRIANGULO')
    if  A==0 or B==0 or C==0:
        pass
elif (A**2 == (B**2)+(C**2)):
    print ('TRINAGULO RETANGULO')
elif (A**2 > (B**2)+(C**2)):
    print ('TRIANGULO OBTUSANGULO')
elif (A**2 < (B**2)+(C**2)):
    print ('TRIANGULO ACUTANGULO')

if A==0 or B==0 or C==0:
    pass
else:
    if(A == B and B == C):
        print("TRIANGULO EQUILATERO")

if((A == B or B == C) and not (A == B and B == C)):
    print("TRIANGULO ISOSCELES")
    
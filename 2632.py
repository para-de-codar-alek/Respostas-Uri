# Receber um valor que vai ser o número de testes
# nesse teste informar a coordenanda (x,y)
# e após o nível da spell e as coordenadas de lançamento
# T <-- inteiro

 
T = int(input())

for l in range(T):

    v1 = [input().split()]

p = int(v1[0])
h = int(v1[1])
x0 = int(v1[2])
y0 = int(v1[3])

v2 = input().split()
spell = str(v2[0])
n = int(v2[1])

xcoordenate = int(v2[2])
ycoordenate = int(v2[3])

if xcoordenate > x0 + p:

    a = xcoordenate - (p+x0)

elif ycoordenate > y0 + h:

    a = ycoordenate - (h+y0)

if spell == "water":

    if n == 1 and a <= 10:

        print("300")

    if n == 2 and a <= 25:

        print("300")

    if n == 3 and a <= 40:

        print("300")

if spell == "fire":

    if n == 1 and a <= 20:

        print("200")

    if n == 2 and a <= 30:

        print("200")

    if n == 3 and a <= 50:

        print("200")

if spell == "earth":

    if n == 1 and a <= 25:

        print("400")

    if n == 2 and a <= 55:

        print("400")

    if n == 3 and a <= 70:

        print("400")

if spell == "air":

    if n == 1 and a <= 18:

        print("100")

    if n == 2 and a <= 38:

        print("100")

    if n == 3 and a <= 60:

        print("100")

else:

    print("0")
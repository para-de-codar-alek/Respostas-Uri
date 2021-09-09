# N <-- número entre 2 e 500.000
# raio = 0
# for l in range(N):
# list = input.split
#x,y <-- list e jogar inteiros em x,y
# if x,y ==

N = int(input())
raio = 0
i = 502
quadrante = [i*[raio] for x in range(i)]
while N:
    N -=1
    x, y = [int(i) for i in input().split()]
    
    if not raio:
        if quadrante[int(x)][int(y)] == 0:
            quadrante [int(x)][int(y)] = 1
        else:
            raio = 1
print(raio)
# Dividir círculos
# Para cada número começando em 1 até 1000 fazer 2*n-1
# N <-- número inteiro
# N1 = 2**(n-1)

N = int(input())
n1 = ((N/12.0)*(N*N*N - 6*N*N + 23*N - 18)/2) + 1
print('{:.0f}'.format(n1))


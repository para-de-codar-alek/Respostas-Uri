# Receber dois números fazer a soma entre os ímpares deles, sem inclui-los, e printar

x = int(input())
y = int(input())
p = 0
for l in range (y+1,x):
    if l % 2 != 0:
        p += l
print (p)
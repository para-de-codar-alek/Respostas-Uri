# Receber valores de x1, y1 e x2, y2 e calcule a distância entre eles, mostrando em 4 float de precisão
import math
linha1 = input().split()
linha2 = input().split()
x1,y1 = linha1
x2,y2 = linha2
dist =math.sqrt(((float(x2)-float(x1))**2)+(float(y2)-float(y1))**2)
print ('{:.4f}'.format(dist))
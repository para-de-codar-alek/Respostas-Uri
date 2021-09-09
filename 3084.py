# Transformar os angulos do relógio em hora e min
# Para cada cora temo 30 graus e para cada min 6
# h <-- angulo da hora
# m <-- angulo do min
# print h e m formatados em :02d
while True:
    try:
        enter = input().split()
        h, m = enter
        h = float(h)
        m = float(m)
        print ('{:02d}:{:02d}'.format(int(h/30), int(m/6)))
    except EOFError:
        break

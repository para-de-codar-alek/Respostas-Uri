while True:
    try:
        height, widith = [int(x) for x in input().split()]
        matriz = []
        for l in range(height):
            matriz.append(input().split())

        num_2 = [(index, w.index('2')) for index, w in enumerate(matriz) if '2' in w]
        num_1 = [(index, w.index('1')) for index, w in enumerate(matriz) if '1' in w]
        x = (abs(num_2[0][0] - num_1[0][0]))
        y = (abs(num_2[0][1] - num_1[0][1]))
        print (f'{y+x}')

    except EOFError:
        break
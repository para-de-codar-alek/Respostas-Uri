from typing import Counter

Counter = 1
while True:
    line = input().split()
    meteoros = 0
    x1, y1, x2, y2 = int(line[0]), int(line[1]), int(line[2]), int(line[3])

    if x1 == x2 == y1 == y2 == 0:
        break
    q = int(input())

    for l in range(q):
        meteoro = input().split()
        x, y = int(meteoro[0]), int(meteoro[1])

        if x1 <= x <= x2:

            if y2 <= y <= y1:
                meteoros += 1

    print(f'Teste {Counter}')
    print(f'{meteoros}')
    Counter += 1
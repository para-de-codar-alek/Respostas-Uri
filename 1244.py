#INCOMPLETO
n = int(input())
for l in range (n):
    start = list(map (str, input (). split ()))
    sort = sorted(start, key=len, reverse=True)
    c = ''
    for l in sort:
        c += l + ' '
    print(c)
    print()
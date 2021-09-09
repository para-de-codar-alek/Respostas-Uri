line = input().split()
teste, visited = line
teste = int(teste)
visited = int(visited)

sailor_visited = list(map(int,input().split()))

while True:
    try:
        visting = int(input())
        if visting  in sailor_visited:
            print(0)
        else:
            print(1)
            sailor_visited.append(visting)
            
    except EOFError:
        break
while True:
    n = int(input())
    if n == 0:
        break
    teams = {}
    for i in range(n):
        entrada = input().split()
        teams[entrada[0]] = int(entrada[1])
    for i in range(n//2):
        partida = input().split()
        classificacao = [int(i)*3 for i in partida[1].split('-')]
        if classificacao[0] > classificacao[1]:
            a = 5
            b = 0
        elif classificacao[0] < classificacao[1]:
            a = 0
            b = 5
        else:
            a = b = 1
        teams[partida[0]] += classificacao[0] + a
        teams[partida[2]] += classificacao[1] + b

    winner = [max(teams, key=teams.get), max(teams.values())]
    if winner[0] == 'Sport':
        print(f'O Sport foi o campeao com {winner[1]} pontos :D')
        print()
    else:
        print(f'O Sport nao foi o campeao. O time campeao foi o {winner[0]} com {winner[1]} pontos :(')
        print()
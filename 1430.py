note_rythm = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64 }

while True:
    rythm = input()
    if rythm == '*':
        break
    rythm = [x for x in rythm.split('/')if x]
    soma = 0

    for notes in rythm:
        time = 0

        for l in notes:
            time+= note_rythm[l]

            if time > 1:
                break

        if time == 1:
            soma+=1
    print(soma)
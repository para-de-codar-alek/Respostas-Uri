n = int(input())

while n:
    n-=1
    diet = input()
    break_f = input()
    lunch = input()
    lunch+= break_f
   
    for l in range(len(lunch)):
        if lunch[l] not in diet:
            diet = 'CHEATER'
            break
        else:
            diet = diet.replace(lunch[l], '')

        if diet != 'CHEATER':
            diet = ''.join(sorted(diet))
        print(diet)
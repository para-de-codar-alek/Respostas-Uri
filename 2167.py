# Inserir números em um tupla em uma range n, se o número posterior
# for menor que o anterior indicar a posição dessa queda

enter = int(input())
line_value = input().split()

for l in range(enter):
    line_value[l] = int(line_value[l])
    if l != line_value.index(line_value[0]):

        if line_value[l]<line_value[l-1]:
            print (l+1)
            break

        elif line_value[l]>=line_value[l-1]:
            if l == enter-1:
                print ('0')
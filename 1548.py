n1 = int(input())

while n1 > 0:
    n1= n1-1
    student = int(input())
    line = input().split()
    for index, l in enumerate(line):
        line[index] = int(line[index])
    students_sort = sorted(line)
    students_sort.reverse()
    value_max = 0

    for index, i in enumerate(line):
        if (line[index]== students_sort[index]):
            value_max+=1
    print(value_max)


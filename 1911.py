i = 1
while i!=0:
    dic = {}
    c = 0
    n = int(input())
    if n == 0:
        i = 0
        break
    else:
        for l in range(n):
            test = {}
            line = input().split()
            student, assign = line
            test[student] = assign
            dic.update(test)
        n2 = int(input())
        for x in range(n2):
            c = 0
            cheking = input().split()
            if cheking[1] in dic[cheking[0]]:
                None
            else:
                verify = cheking[1].split()
                verify2 = dic[cheking[0]]
                verify2 = verify2.split()
                for item in verify:
                    for item1 in verify2:
                        if item == item1:
                            None
                        else:
                            c+1
                            if c>1:
                                final = 1
                                break
                 

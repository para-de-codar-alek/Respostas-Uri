from math import ceil

def criptografia(a):

    b =''
    for x in a:

        if (x.isalpha() == True): 
            b += chr(ord(x) + 3)
                               
        else:
            b+= x
    
    c = b[::-1]
    d = ceil(len(c)/2)
    e = c[-d:] 
    f = ''

    for i in e:
        f+= chr(ord(i)-1) 
    cripted = c.replace(e,f)
    return cripted
n = int(input())

for p in range(n):
    a = str(input())
    criptografia(a)
    print(criptografia(a))
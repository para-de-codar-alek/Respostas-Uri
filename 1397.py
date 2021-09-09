
from typing import NoReturn


i=0

while i==0:
    N = int(input())
    if N==0:
        break
    p1 = 0
    p2 = 0
    for l in range(N):
        line = input().split()
        A, B = line
        A = int(A)
        B = int(B)
        if A>B:
            p1+=1
        elif B>A:
            p2+=1
        elif B==A:
            None
    print (p1,p2)
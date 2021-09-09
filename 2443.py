line = input().split()
a,b,c,d = line
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b==d:
    s = a+c
    if s%b == 0:
        print (f'{s/b:.0f} {1}')
    else:
        for i in range (1,s):
            if s % i == 0 and b % i == 0:
                s = s/i
                b = b/i
        print(f'{s:.0f} {b:.0f}')
else:
    den = b*d
    v = d*a
    w = b*c
    s = v+w
    print (s, w, v, den)
    if s % den == 0:
        print (f'{s/den:.0f} {1}')
    else:
        for i in range (1,den+1):
            if s % i == 0 and den % i == 0:
                s = s/i
                den = den/i
        print(f'{s:.0f} {den:.0f}')
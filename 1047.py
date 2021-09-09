line = input().split()
h1, s1, h2, s2 = line
h1 = int(h1)
s1 = int(s1)
h2 = int(h2)
s2 = int(s2)
if h1<h2:
    h = h2-h1
    if s1<s2:
        s= s2-s1
    if s1>s2:
        h = h-1
        s = (60 - s1)+ s2
    if s1==s2:
        s = 0
if h1>h2:
    h = (24-h1) + h2
    if s1 < s2:
        s = s2 - s1
    if s1 > s2:
        h = h-1
        s = (60-s1) + s2
  
if h1==h2:
    if s1 < s2:
        s = s2 - s1
        h = 0
    if s1 > s2:
        s = (60-s1) + s2
        h = 23
    if s1 == s2:
        h = 24
        s = 0
print ('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h,s))
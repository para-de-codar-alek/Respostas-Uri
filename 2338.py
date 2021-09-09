morse_list = {'=.===' : 'a' , '===.=.=.=' : 'b' ,  '===.=.===.=' : 'c' ,  '===.=.=' : 'd' , '=' : 'e' ,  '=.=.===.=' : 'f' , 
'===.===.=': 'g' ,  '=.=.=.=':'h' , '=.=' : 'i' , '=.===.===.===' : 'j' , '===.=.===': 'k' , '=.===.=.=' : 'l' ,  
'===.===' : 'm', '===.=': 'n'  , '===.===.===' : 'o' , '=.===.===.=' : 'p' , '===.===.=.===' : 'q' , '=.===.=' : 'r' , 
'=.=.=' : 's' , '===' : 't' , '=.=.===' : 'u' ,  '=.=.=.===' : 'v' ,  '=.===.===' : 'w' ,  '===.=.=.===' : 'x', 
'===.=.===.===' : 'y' , '===.===.=.=' : 'z' }

n = int(input())

for l in range(n):
    morse = input().split('.......')

    for code in range(len(morse)):
        decod = morse[code]
        decod = decod.split('...')

    for i in range(len(decod)):
        print(morse_list[decod[i]], end='')
    
    if code != len(morse) - 1:
        print (end='')
print()


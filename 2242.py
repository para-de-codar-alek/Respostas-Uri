init = input()
vowels = ''
for l in init:
    if (l=='a' or l == 'e' or l == 'i' or l=='o' or l=='u'):
        vowels+=l
if (vowels == vowels[::-1]):
    print(f'S')
else:
    print(f'N')
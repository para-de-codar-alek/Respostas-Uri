N = int(input())
broken_plates = 0
while N > 0:
    N -= 1
    x, y = input().split()
    if int(y) < int(x):
        broken_plates+=int(y)

print(broken_plates)
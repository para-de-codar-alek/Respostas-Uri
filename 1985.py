precos =  {'1001': 1.50, '1002': 2.50, '1003': 3.50, '1004': 4.50, '1005': 5.50}
n = int(input())
value = 0
for l in range(n):
    line = input().split()
    product, qtt = line
    qtt = int(qtt)
    price = precos[product] * qtt
    value+= price
print(f'{value:.2f}')

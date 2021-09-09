N = int(input())

value1 = N // 100
next_value = N % 100

value2 = next_value // 50
next_value2 = next_value % 50

value3 = next_value2 // 20
next_value3 = next_value2 % 20

value4 = next_value3 // 10
next_value4 = next_value3 % 10

value5 = next_value4 // 5
next_value5 = next_value4 % 5
value6 = next_value5 // 2

next_value6 = next_value5 % 2

print (N)
print (f'{value1} nota(s) de R$ 100,00')
print (f'{value2} nota(s) de R$ 50,00')
print (f'{value3} nota(s) de R$ 20,00')
print (f'{value4} nota(s) de R$ 10,00')
print (f'{value5} nota(s) de R$ 5,00')
print (f'{value6} nota(s) de R$ 2,00')
print (f'{next_value6} nota(s) de R$ 1,00')

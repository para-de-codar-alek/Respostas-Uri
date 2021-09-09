N = float(input())
 
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

value7 = next_value6 // 1
next_value7 = next_value6 % 1

value8 = next_value7 //0.5
next_value8 = next_value7 % 0.5

value9 = next_value8 // 0.25
next_value9 = next_value8 % 0.25

value10 = next_value9 // 0.10
next_value10 = next_value9 % 0.10

value11 = next_value10 // 0.05
next_value11 = next_value10 % 0.05

value12 = next_value11 /0.01
print ('NOTAS:')
print (f'{value1:.0f} nota(s) de R$ 100.00')
print (f'{value2:.0f} nota(s) de R$ 50.00')
print (f'{value3:.0f} nota(s) de R$ 20.00')
print (f'{value4:.0f} nota(s) de R$ 10.00')
print (f'{value5:.0f} nota(s) de R$ 5.00')
print (f'{value6:.0f} nota(s) de R$ 2.00')
print ('MOEDAS:')
print (f'{value7:.0f} moeda(s) de R$ 1.00')
print (f'{value8:.0f} moeda(s) de R$ 0.50')
print (f'{value9:.0f} moeda(s) de R$ 0.25')
print (f'{value10:.0f} moeda(s) de R$ 0.10')
print (f'{value11:.0f} moeda(s) de R$ 0.05')
print (f'{value12:.0f} moeda(s) de R$ 0.01')
matriz = []
sum_ = 0.0
index = int(input())
operation = input()
for i in range(12):
  lista = []
  for j in range(12):
    number_ = float(input())
    lista.append(number_)
  matriz.append(lista)

for a in range(12):
  for b in range(12):
    if a == index:
      sum_+=matriz[a][b]

if operation == "S":      
  print(f"{sum_:.1f}")      
elif operation == "M":
  print(f"{sum_/12:.1f}")

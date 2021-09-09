# days <-- quantidade de dias
# year <-- days//2
# n1 <-- days%2
# month <-- n1//30
# n2 <-- n1%30
# dias <-- n2//2, printar year \n month \n dias
days = int(input())
year = days//365
n1 = days%365
month = n1//30
n2 = n1%30
dias = n2
print ('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(year,month,dias))
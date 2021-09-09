# Converter segundos em horas minutos e segundos
# Ler segundos
# Fazer divisão por resto e guardar na variavel
# criar outra var para min com  
time = int(input())
hora = time//3600
min = time-hora*3600
minn = min//60
seg = time-hora*3600-minn*60
print ('{}:{}:{}'.format(hora, minn, seg))
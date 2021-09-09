# O angulo do Sol/lua mede a parte do dia
# ang <-- entrada do ângulo 0 a 360
# Se ang>=0 and ang<90 or ang==360 print manhã
# Se ang>=90 and ang<180 print tarde
# Se ang>=180 and ang<270 print noite
# senão print madrugada
while True:
    try:
        M = float(input())
        if (M >= 0 and M< 90 or M== 360):
            print ('Bom Dia!!')
        elif (M >= 90 and M< 180):
            print ('Boa Tarde!!')
        elif (M >= 180 and M< 270):
            print ('Boa Noite!!')
        elif (M >=270 and M< 360):
            print ('De Madrugada!!')
    
    except EOFError:
        break
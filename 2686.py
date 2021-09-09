while True:
    try:
        M = float (input())
        M1 = M 
        hora = ((M1 * 240)/ 3600) % 60
        min = ((M1 * 240)/ 60) % 60
        M1 = (M1 * 240) % 60

        
        if (M >= 0 and M< 90 or M== 360):
            print ('Bom Dia!!')
            print ('{:02d}:{:02d}:{:02d}'.format(int((hora+6))%24,int(min),int(M1)))
        elif (M >= 90 and M< 180):
            print ('Boa Tarde!!')
            print ('{:02d}:{:02d}:{:02d}'.format(int((hora+6))%24, int(min), int(M1)))
        elif (M >= 180 and M< 270):
            print ('Boa Noite!!')
            print ('{:02d}:{:02d}:{:02d}'.format(int((hora+6))%24, int(min),int (M1)))
        elif (M >=270 and M< 360):
            print ('De Madrugada!!')
            print ('{:02d}:{:02d}:{:02d}'.format(int((hora+6))%24, int(min), int(M1)))
    
    except EOFError:
        break
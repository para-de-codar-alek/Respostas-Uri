l1 = input()
l2 = input()
l3 = input()

if l1 == ('invertebrado'):
    if l2 == ('inseto'):
        if l3 == ('hematofago'):
            print ('pulga')
        elif l3 == ('herbivoro'):
            print ('lagarta')
    elif l2 == ('anelideo'):
        if l3 == ('hematofago'):
            print ('sanguessuga')
        elif l3 == ('onivoro'):
            print ('minhoca')
elif l1 == ('vertebrado'):
    if l2 == ('ave'):
        if l3 == ('carnivoro'):
            print ('aguia')
        elif l3 == ('onivoro'):
            print ('pomba')
    if l2 == ('mamifero'):
        if l3 == ('onivoro'):
            print ('homem')
        if l3 == ('herbivoro'):
            print ('vaca')
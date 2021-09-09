# Receber as 4 notas de um aluno, N1=2*nota, N2=3*nota, N3=4*nota e N4=1*nota
# Se o aluno estiver com nota menor que 5, reprovado
# entre 5 e 6,9 (incluídos), em exame, se em exame pedir outra nota e somar com a primeira media e dividir por 2
# e dar o resultado se maior que 5 aprovado, senão reprovado
#  maior que 7 aprovado
# line == input().split()
# N1, N2, N3 e N4 <-- line
# Transformar N1,N2,N3 e N4 em floats
# Media = 2*N1+3*N2+4*N3+1*n4/10
# se media > 7 print aprovado, se media <5 reprovado, se média entre 5 e 6.9 o aluno entra em exame
# exame <-- nota do exame, median = Media+exame/2, se maior que 5 aprovado senão reprovado
list = input().split()
N1, N2, N3, N4 = list

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

nota_exame = 0.0
media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print ('Media: {:.1f}'.format(media))

if (media >= 7.0):
    print ("Aluno aprovado.")

if (media < 5.0):
    print ("Aluno reprovado.")

if (media >= 5.0 and media <= 6.9):
    print ("Aluno em exame.")
    nota_exame = float(input())
    print ("Nota do exame: {:.1f}".format(nota_exame))
    media = (nota_exame+media)/2
    
    if (media >= 5.0):
        print ("Aluno aprovado.")
    else:
        print ("Aluno reprovado.")
    print ("Media final: {:.1f}".format(media))

    
#9.0 4.0 8.5 9.0
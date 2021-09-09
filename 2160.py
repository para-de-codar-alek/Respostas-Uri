#Preencher formulários é uma tarefa simples. 
# Mas é preciso conferir se o espaço reservado para os dados é suficiente.
#Sua tarefa é, dada uma linha de texto, indicar se ele cabe ou não cabe em um formulário com 80 caracteres.
# txt <-- texto
# tam <-- len(txt)
# Se txt > 80 caracteres print no, senão yes
txt = str(input())
tam = len(txt)
if tam>80:
    print('NO')
else:
    print('YES')
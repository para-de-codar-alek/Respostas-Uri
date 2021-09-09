snacks = [[0],['Cachorro Quente', 4.00],['X-salada', 4.50],['X-Bacon', 5.00],['Torrada simples', 2.00],['Refrigerante', 1.50]]
line = input().split()
code_snacks, qtd = line
code_snacks = int(code_snacks)
qtd = int(qtd)

final_price = qtd*snacks[code_snacks][1]

print(f'Total: R$ {final_price:.2f}')



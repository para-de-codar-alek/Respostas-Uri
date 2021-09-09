x = float(input())
if x <= 2000.00:
    y = 0
    print ('Isento')
if x > 2000.00 and x <= 3000.00:
    y2 = x - 2000.00
    y = y2 * 0.08
if x > 3000.00 and x <= 4500.00:
    y2 = 1000.00 * 0.08
    y3 = x - 3000.00
    y = (y3 * 0.18) + y2
if x > 4500.00:
    y2 = 1000.00 * (0.08)
    y3 = 1500.00 * (0.18)
    y4 = x - 4500.00
    y = y3 + y2 + (y4 * 0.28)
if x > 2000:
    y = float(y)
    print ('R$ {:.2f}'.format(y))

# 3.	Создайте программу для игры в "Крестики-нолики".

 1 2 3
   4 5 6
   7 8 9
спрашиваете, куда хочет ходить, на какую ячейку ставит
][x, -, -], [-, - ,-], [-, -, -]]

как обратиться к индексам:

sp = [['x', '0", 'x'], [0, -,x], [x, x, x]]
sp[1][1] = '0'
sp[0][2] = '0'
print(*sp, sep='\n')


проверка:

sp[0][0] == sp[0][1] ==sp[0][2]!='-'
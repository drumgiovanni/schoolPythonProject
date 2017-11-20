table = [[100, 50, 32, 25],
         [80, 45, 99, 12],
         [3, 43, 18, 9]]
result = []
list = table[0]
k = 0
for j in range(len(list)):
    for i in range(len(table)):
        k += table[i][j]
        if  i == len(table) -1:
                result.append(k)
                k = 0
print(result)


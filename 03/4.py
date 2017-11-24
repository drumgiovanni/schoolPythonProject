x = [2, 4, 6, 8]
y = [2, 4, 5, 7, 9]
z = []
for i in x:
    if i not in y:
        z.append(i)
z += y
print(z)
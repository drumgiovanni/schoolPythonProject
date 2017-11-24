i = 1
while i <= 50:
    if i % 3 == 0 and i % 5 == 0:
        print("○●")
    elif i % 3 == 0 and not i % 5 == 0:
        print("○")
    elif i % 5 == 0 and not i % 3 == 0:
        print("●")
    else:
        print(i)
    i += 1
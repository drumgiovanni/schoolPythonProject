for i in range(1,2):
    print(" ")
    for j in range(1,10):
        print("{:>7}".format(i * j),end =" ")
        if j == 1 :
            print("|",end=" ")
for i in range(2,3):
    print("\n" + "- " * 4 + "+" + "- " * 33)
    for j in range(1,10):
        print("{:>7}".format(i * j), end=" ")
        if j == 1 :
            print("|",end=" ")
for i in range(3,10):
    print(" ")
    for j in range(1,10):
        print("{:>7}".format(i * j),end =" ")
        if j == 1 :
            print("|",end=" ")
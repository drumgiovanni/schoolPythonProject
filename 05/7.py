with open("data0502.txt", mode="r", encoding="utf-8") as d:
    for i in d:
       text = i.rstrip("\n")
       line = text.split(",")
       num = 0
       for j in line:
           if num < int(j):
               num = int(j)
       print(num)


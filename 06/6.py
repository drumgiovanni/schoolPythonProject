
with open("workers.txt",mode="r",encoding="utf-8") as f:
    laborlist = {}
    for i in f:
        text = i.rstrip("\n")
        list = text.split("\t")
        x = list[0]
        y = int(list[1])
        if x in laborlist:
            laborlist[x] += y
        else:
            laborlist[x] = y
    for j in laborlist:
        print(j, laborlist[j])
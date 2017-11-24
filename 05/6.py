with open("news.txt", mode="r", encoding="utf-8") as f:
    count = {}
    for j in f:
        list = j.split()
        for i in list:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
    for x in count:
        print(x, count[x])
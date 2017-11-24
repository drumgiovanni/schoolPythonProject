st = ["天王寺", "美章園", "南田辺", "鶴ヶ丘", "長居", "我孫子町", "杉本町"]
fst = int(input("どこから？"))
lst = int(input("どこまで？"))

while fst <= lst:
    print(fst, st[fst])
    fst += 1
with open("data0501.txt", mode="r", encoding="utf-8") as d:
    sum = 0
    for i in d:
        print(i)
        sum += int(i)
print(f"合計は{sum:d}でした")

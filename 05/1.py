import random
with open("data0501.txt", mode="w", encoding="utf-8") as f:
    for i in range(0,10):
        rnd = str(random.randrange(999)) + "\n"
        print(rnd)
        f.write(rnd)
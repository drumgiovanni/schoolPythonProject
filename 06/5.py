with open("workers.txt",mode="a",encoding="utf-8") as f:
    while True:
        name = input("お名前を入力してください：　")
        if name == "END":
            break
        time = input("働いた時間を入力してください：　")
        f.write(f"{name}\t{time}\n")

    
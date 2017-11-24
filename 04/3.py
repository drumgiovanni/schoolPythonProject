while True:
    sent = input("英文を入力してください： ")
    if sent == "END":
        break
    words = len(sent.split(" "))
    print(words)
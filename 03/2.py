dic = {}
while True:
    key = input("キーを入力してください：　")
    if key == "END":
        break
    val = input("値を入力してください：　")
    dic[key] = val
for item in dic.keys():
    print(item, dic[item])
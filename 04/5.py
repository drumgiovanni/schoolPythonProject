q = {1:"1日は何時間か？　\n\t 1.18時間  2.22時間  3.24時間", 2:"日本とイギリスの時差は何時間か？\n\t1.2時間  2.9時間  3.14時間", 3:"野の花ハウスでホットコーヒーはいくらで売られているか？\n\t1.100円  2.110円  3.120円"}
a = {1:3, 2:2, 3:1}
n = 0
for i in q:
    print(q[i])
    x = input("解答を入力してください： ")
    if int(x) == a[i]:
        print("おめでとうございます。正解です！")
        n += 1
    else:
        print("ザンネーン。不正解！")
rate = (n/len(q))
print(f"正答率は{rate:6.1%} でした")
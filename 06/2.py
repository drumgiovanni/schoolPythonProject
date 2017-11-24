n = int(input("好きな数字を入力してください：　"))
x = 0
for i in range(n+1):
    if i <= (n+1)/2:
        print("#" * i)
        x += 1
    if i > (n+1)/2:
        print("#" *(n-x+1))
        x += 1
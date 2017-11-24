a = int(input("整数を入力してください"))
b = int(input("整数を入力してください"))
c = int(input("整数を入力してください"))
if a < b +c and b < a + c and c < b + a:
    print("a,b,cを辺とする三角形が成り立ちます")
else:
    print("a,b,cを辺とする三角形が成り立ちません")
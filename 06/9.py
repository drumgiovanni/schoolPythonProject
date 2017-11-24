print("""【数値当てゲーム】
        パソコンが1~100の数値をランダムで用意します。
        どの数字が用意されるか予測してみよう！！""")
import random
rnm = int(random.randrange(100))
time = 1
while True:
    suspect = int(input("パソコンが用意した数値を予測してください：　"))
    if suspect == rnm:
        print(f"正解です {time}回目で正解しました。")
        break
    elif suspect < rnm:
        print("小さすぎます。")
        time += 1
    else:
        print("大きすぎます。")
        time += 1
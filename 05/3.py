import random                       #ランダムモジュールをインポート
rnd = int(random.randrange(15))     #15までの乱数をintに変換しrndに代入　→　のちに複数回関数を実行するため

def func1(x, y):                    #関数を定義
    return print(x**2 + y**2)


for i in range(rnd):                #関数をrnd回実行し、実行するたびx,yの中身がランダムにかわるようにした。
    x = int(random.randrange(120))
    y = int(random.randrange(399))
    print(f"x={x},y={y}", end = " => ")
    func1(x, y)
print("\n" + f"今回は、{rnd}回実行されました")
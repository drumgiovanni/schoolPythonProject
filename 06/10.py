import random

while True:
    rnm = random.randrange(3)
    if rnm == 1:
        pchand = "G"
    elif rnm == 2:
        pchand = "C"
    else:
        pchand = "P"
    humanhand = input("グーならばG、チョキならばC、パーならばPを入力してください")
    if not humanhand == pchand:
        if humanhand == "G":
            if pchand == "C":
                print("あなたはグー、わたしはチョキを出しました")
                print("あなたの勝ちです")
                break
            else:
                print("あなたはグー、わたしはパーを出しました")
                print("わたしの勝ちです")
                break
        elif humanhand == "C":
            if pchand == "G":
                print("あなたはチョキ、わたしはグーを出しました")
                print("わたしの勝ちです")
                break
            else:
                print("あなたはチョキ、わたしはパーを出しました")
                print("あなたの勝ちです")
                break
        else:
            if pchand == "C":
                print("あなたはパー、わたしはチョキを出しました")
                print("わたしの勝ちです")
                break
            else:
                print("あなたはパー、わたしはグーを出しました")
                print("あなたの勝ちです")
                break
    elif pchand == humanhand:
        print("あいこです")
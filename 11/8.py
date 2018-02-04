import random
def master_mind():
    ballList = ['赤', '青', '緑', '黄', '紫', '白']
    rancolor = random.sample(ballList, 4)
    ranList = ''.join(rancolor)
    count = 0
    print("""赤、青、緑、黄、紫、白から４色を選択し、例のように並べてください
例）＞ 青白緑赤""")
    while True:
        inpList = input("＞")
        out = ""
        if len(set(inpList) & set(ballList)) < 4:

            for i in range(0,len(inpList)):
                if not inpList[i] in ballList:
                    out = inpList[i]
                    print(f"{out}は存在しません。もう一度入力してください。")
                elif len(inpList) < 4:
                    print("ちゃんと4つ選んでください。")
            continue
        elif len(set(inpList)) <= 3:
            print(f"重複しています。もう一度入力してください。")
            continue
        hit = 0
        blow = 0
        if inpList == ranList:
            print(f"おめでとう！{count}回目で正解しました。")
            break
        for i in range(0,len(inpList)):
            if inpList[i] == ranList[i]:
                hit += 1
                count += 1
            elif inpList[i] in ranList:
                blow += 1
                count += 1
        print(f"Hit: {hit}, Blow: {blow}")
master_mind()

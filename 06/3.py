import random
rnd = int(random.randrange(9))
ball = {1:"赤玉", 2:"赤玉", 3:"赤玉", 4:"赤玉", 5:"赤玉", 6:"白玉", 7:"白玉", 8:"白玉", 9:"黄玉"}
print(f"{ball[rnd]}が出ました")
if rnd <= 5:
    print("はずれです")
elif rnd > 5 and rnd <= 8:
    print("当たりです")
else:
    print("大当たりです")

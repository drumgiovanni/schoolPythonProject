word = input("好きな英単語（動詞）を入力してください： ")
words = word.split()
if words[-1] == "y":
    words[-1] = "ied"
elif words[-1] == "e":
    words.append("d")
else:
    words.append("ed")
result = ""

for i in words:
    result += i
print(result)


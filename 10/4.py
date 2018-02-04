import re
import urllib.request

url = "http://shakespeare.mit.edu/hamlet/hamlet.1.3.html"
encoding="utf-8"
proxy = {"http": "http://prxy.ex.media.osaka-cu.ac.jp:10080",
         "https": "http://prxy.ex.media.osaka-cu.ac.jp:10080"}

with urllib.request.FancyURLopener(proxy).open(url) as fh:
    count = {}
    wlen = 0
    longword = []
    wsum = 0
    for rawline in fh:
        line = rawline.decode(encoding).rstrip()
        match = re.search(r"<A NAME=[0-9]+>(.+)</A>", line)
        if match:
            sentence = match.group(1).lower()
            sentence = re.sub(r"[.,?!:;]", "", sentence)
            for words in sentence.split():
                count.setdefault(words, 0)
                count[words] = count[words] + 1
    for wnum in count:
        if len(wnum) > wlen:
            wlen = len(wnum)
            longword = wnum
        elif len(wnum) == wlen:     #もっとも長い単語が２つ以上の場合
            longword.append(wnum)   #リストにそのまま代入すると消えてしまうので、appendする
        wsum += count[wnum]
    wave = wsum / len(count)        #lenでcountの要素の数を取得し、平均を求める
    cthe = count["the"]             #countに入っているtheの値を取り出す
    print("1.に対する答え" + "\n" + "  最も長い単語は", longword, "で、",wlen, "文字")
    print("2.に対する答え" + "\n" + "  1単語あたりの平均文字数は", wave)
    print("3.に対する答え" + "\n" + "  定冠詞theは", cthe, "個")
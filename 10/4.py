import re
import urllib.request

url = "http://shakespeare.mit.edu/hamlet/hamlet.1.3.html"
encoding="utf-8"
proxy = {"http": "http://prxy.ex.media.osaka-cu.ac.jp:10080",
         "https": "http://prxy.ex.media.osaka-cu.ac.jp:10080"}

def CountWords(dic, key):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1
def Longword()

with urllib.request.FancyURLopener(proxy).open(url) as fh:
    count = {}
    wlen = 0
    longword = []
    for rawline in fh:
        line = rawline.decode(encoding).rstrip()
        match = re.search(r"<A NAME=[0-9]+>(.+)</A>", line)
        if match:
            sentence = match.group(1).lower()
            sentence = re.sub(r"[.,?!:;]", "", sentence)
            for words in sentence.split():
                CountWords(count, words)
    for j in count:
        if len(j) > wlen:
            wlen = len(j)
            longword =j
    print("最も長い単語は", longword, wlen)
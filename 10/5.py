import urllib.request
import re

url = "https://weather.yahoo.co.jp/weather/jp/27/6200.html"
encoding = "utf-8"

def fetch(i,a):
    a = i.decode(encoding)
    match = re.search(r".*", a)
    if match:
        info = match.group()
        wf.write(info + "\n")


with urllib.request.FancyURLopener().open(url) as rf:
    with open("weatherforecast.html", mode="a", encoding="utf-8") as wf:
        for i in rf:
            fetch(i, "line1")
            if b"<body" in i:
                break

        for i in rf:
            if b"id=\"yjw_week\"" in i:
                for i in rf:
                    if b"</table>" in i:
                        break
                    fetch(i, "line2")

with urllib.request.FancyURLopener().open(url) as rf:                       #なぜか上と同様for文を用いて処理をし用としたが、うまくいかなかったため、こうした。
    with open("weatherforecast.html", mode="a", encoding="utf-8") as we:    #具体的にどうなったかというと、エラーは発生しないが、for i in rf:の下にprintを書いても何も表示されない、つまり通っていなかった。
        for i in rf:                                                        #for文以上の２文を追記したところうまくいくようになった。
            if b"</body>" in i or b"</html>" in i:
                a = i.decode(encoding)
                match = re.search(r".*", a)
                if match:
                    info = match.group()
                    we.write(info + "\n")

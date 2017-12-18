import re
import urllib.request

url = "https://www.ips.media.osaka-cu.ac.jp/?page_id=180"
encoding="utf-8"
proxy = {"http": "http://prxy.ex.media.osaka-cu.ac.jp:10080",
         "https": "http://prxy.ex.media.osaka-cu.ac.jp:10080"}

count = 0
with urllib.request.FancyURLopener(proxy).open(url) as fh:
    for l in fh:
        line = l.decode(encoding).rstrip()
        match = re.search(r"<h[1-6]>", line)
        if match:
            count += 1
print(count)
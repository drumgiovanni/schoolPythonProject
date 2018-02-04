import re
import urllib.request

url = "https://www.ips.media.osaka-cu.ac.jp/?page_id=665l"
encoding="utf-8"
"""proxy = {"http": "http://prxy.ex.media.osaka-cu.ac.jp:10080",
         "https": "http://prxy.ex.media.osaka-cu.ac.jp:10080"}"""

urls = []
with urllib.request.FancyURLopener().open(url) as fh:
    for l in fh:
        line = l.decode(encoding).rstrip()
        match = re.search(r"<a href=\"(.+)\">.+</a>", line)
        if match:
            link = match.group(1)
            urls.append(link)
for i in urls:
    print(i)
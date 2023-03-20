import os
import re

import requests

header = {
    "User-Agent":
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/80.0.3987.122 Safari/537.36',
    'Accept':
    '*/*',
    'Accept-Language':
    'en-US,en;q=0.8',
    'Cache-Control':
    'max-age=0',
    'Connection':
    'keep-alive'
}
f = open("/root/vis/1006.txt")
line = f.readlines()
for i in range(0, len(line), 1):
    title = re.findall(r'(_preview_.+\.m4a)', line[i].strip())
    if len(title) != 0:
        title = line[i].strip().replace(title[0], '.m4a').replace(
            'audiofreepay.ali.xmcdn.com', 'audiopay.cos.tx.xmcdn.com')
    else:
        title = line[i].strip()
    print(title)
    url = title
    path = "home/content"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + str("%03d" % i) + '.m4a', 'wb') as f:
        f.write(requests.get(url, headers=header).content)

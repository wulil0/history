import requests
import re
import os
import math

hea = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
}
path = "/Users/ll/jfz/"
file = sorted(os.listdir(path))
url0 = 'https://www.ximalaya.com/album/45019315/p{}'
a = requests.get(url0.format('0'), headers=hea)
num = re.findall('trackTotalCount":(\d+),"', a.text)
content = []
num = math.ceil(int(num[1]) / 30) + 1

for i in range(1, num):
    url = url0.format(str(i))
    a = requests.get(url, headers=hea)
    title = re.findall('<span class="title _nO">(.+?)</span>', a.text)
    title = re.findall(
        '"index":\d+,"trackId":\d+,"isPaid":true,"tag":\d+,"title":"(.+?)","playCount":\d+,"showLikeBtn":true,"isLike":false,"showShareBtn":true,"showCommentBtn":true,"showForwardBtn":false',
        a.text)
    if (len(title) != 0):
        content = content + title
# print(len(content))

for f, t in zip(file, content):
    myfile = os.path.join(path, str(f))
    oldName = str(f)[:3]
    newName = os.path.join(path, oldName + str(t).replace('|', ' ') + '.m4a')
    print(newName)
    # print(os.path.join(path, str(t).replace('|', ' ') + '.m4a'))
    os.rename(myfile, newName)

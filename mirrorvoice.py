import requests
import re
import os
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome_options=Options()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.get(url)
# body = browser.page_source
# name = re.findall(r'(ep\d+_.+?_\d+)',body)

hea = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
}

url = 'https://www.mirrorvoice.com.tw/audiobooks/437'
body = requests.get(url)
body = body.text
with open('a.html', 'w+') as f:
    f.write(body)

# name = re.findall(r'name:"(\d+[\.|_].+?)"', body)
name = re.findall(r'name:"(\d+[\.|_| ].+?)"', body)
if len(name) == 0:
    name = re.findall(r'name:"(EP\d+.+?)",', body)

print(name)

f = open("url.txt")
lines = f.readlines()
path = '/Users/ll/Downloads/穿越臺灣趣歷史：從猛獁象到斯卡羅，考古最在地的臺灣史/'
for i in range(0, len(name), 1):
    l = lines[i].replace('\n', '')
    ll = l.split('/')[-1]
    os.rename(path + ll, path + name[i] + '.mp3')

# file = os.listdir(path)
# for ff in file:
#     os.rename(path+ff,path+ff+".mp3")

# text = browser.find_element_by_xpath('//*[@id="audiobooks-intro"]/div/div[2]/ul')
# for t in text:
#     print(t)
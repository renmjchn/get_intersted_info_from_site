#标签属性修改版

import requests
from bs4 import BeautifulSoup

url = 'http://bbs.lol.qq.com/forum.php?mod=forumdisplay&fid=40'
site = 'http://bbs.lol.qq.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
response = requests.request('GET', url, headers = headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
lines = soup.find_all('a', onclick="atarget(this)")
text_bf = '''<!DOCTYPE html>
<html>
<head>
<meta charset="gbk">
<title>英雄联盟论坛帖子目录</title>
</head>
<body>'''
text_end = '''</body>
</html>'''
with open('目录.html', 'w', ) as f:
    f.write(text_bf)
for i in lines:
    soup2 = BeautifulSoup(str(i), 'html.parser')
    del soup2.a['class']
    del soup2.a['onclick']
    del soup2.a['style']
    soup2.a['href'] = site + soup2.a['href']
    soup2.string.replace_with(str(lines.index(i) + 1) + '$$' + soup2.string)
    text = '<p> ' + str(soup2.a) + '</p>'
    print(text)
    with open('目录.html', 'a+', ) as f:
        f.write(text)
with open('目录.html', 'a+', ) as f:
    f.write(text_end)


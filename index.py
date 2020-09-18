from bs4 import BeautifulSoup
import requests

# URL取得 ソース取得
URL = "https://honmono-eigo.com/word3000/quickresponse1"
resp = requests.get(URL)
soup = BeautifulSoup(resp.text, features="html.parser")

# tdタグを取得 & tdの数
len = len(soup.find_all("td"))
x = soup.find_all("td")

# リスト & タグ削除
l = []
for i in x:
  l.append(i.text)

# 日本語と英語　リスト
a = [l[i:i+2] for i in range(0,len,2)]


for i in a:
  print('......'.join(i))
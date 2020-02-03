import requests
from bs4 import BeautifulSoup
import re 
ua = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
r = requests.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=病毒",headers=ua)
print(r.status_code)
print(type(r.text),type(r.content.decode("utf-8")))

response = r.content.decode("utf-8")
#print(response)
soup = BeautifulSoup(response, 'html.parser')
rsEle= soup.select("#rs")
print(rsEle[0],'rsele')
rsSoup = BeautifulSoup(str(rsEle[0]),"html.parser")
ancs=rsSoup.find_all('a')
for a in ancs:
    
    x=re.findall('<a href=(.*?)>(.*?)</a>',str(a))[0]
    print(x[1])
# print([i for i in rsSoup])

from time import sleep
import requests
import math
import re
from bs4 import BeautifulSoup


if __name__=="__main__":
    r = requests.get("https://www.apple.com/ua/macbook-pro-14-and-16/specs/")
    page = BeautifulSoup(r.text,'html.parser')
    res = page.find_all('div',attrs={'class': 'techspecs-row'})
    res = res[:len(res)//2]
    for text in res:
        t = re.sub("[^\w]", " ", text.text).split()
        str = set(t)
        print(text.div.text.strip(), math.floor(len(str)/len(t)*100), "%", sep=' ')
        
   





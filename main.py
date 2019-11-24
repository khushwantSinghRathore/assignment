import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bewakoof.com/desi-collection')
print(req.status_code)
# print(req.content)

bs = BeautifulSoup(req.content,'html.parser')
# print(bs.prettify())
fp = open("fileName.csv","w")
fp.write('t-shirt ,  price  , image \n')


for i in bs.find_all('div',{'class' : 'productCardBox'}):
    for addr in i.find_all('div',{'class' : 'productCardImg'}):
        for Tname in bs.find_all('div',{'class' : 'productCardDetail'}): 
            var = addr.find_all('img')
            for j in var:
                print(j.get('src'))
                fp.write(str(Tname.find_all('h3')[0].text))
                fp.write(',')
                fp.write(str(Tname.find_all('b')[0].text))
                fp.write(',')
                fp.write(str(j.get('src')))
                fp.write('\n')




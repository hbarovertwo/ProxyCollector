import requests
from bs4 import BeautifulSoup

n = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/')
soup = BeautifulSoup(n.text, 'html.parser')
a = soup.find_all(class_='useragent')

na = requests.get('https://www.us-proxy.org/')
woop = BeautifulSoup(na.text, 'html.parser')
x = woop.find('table')
z = x.find_all('td')

proxlist = []
portlist = []
proxies = []
for i in range(0,1600,8):
    proxlist.append(z[i].text)
for i in range(1,1600,8):
    portlist.append(z[i].text)
for i in range(0,len(proxlist)):
    proxies.append(proxlist[i]+':'+portlist[i])

finalproxlist = []
for i in range(0,200):
    emp = {}
    emp['address'] = proxies[i]
    finalproxlist.append(emp)


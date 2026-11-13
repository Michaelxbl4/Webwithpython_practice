from bs4 import BeautifulSoup
import urllib.request,urllib.parse, urllib.error
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input("Enter url name: ")
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('td')
sum=0
for tag in tags:
    soup_=BeautifulSoup(tag.decode(),'html.parser')
    numbers=soup_.find('span')
    if(numbers is not None):
        try:
            sum+=int(numbers.contents[0])
        except:
            sum+=0
print(sum)
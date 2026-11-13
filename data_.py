import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input("Enter url name: ")
repetition=input("Enter number of repetition: ")
position=input("Enter link position: ")
repetition=int(repetition)
position=int(position)
CurrentPosition=0
Repeated=0
while Repeated <repetition:
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup.findAll('a')
    print("Retrieving:",url)
    url=str(tags[position-1].get('href',None))
    Repeated+=1
print("Retrieving:",url)
print("Answer",(url.split('.')[-2]).split('_')[-1])
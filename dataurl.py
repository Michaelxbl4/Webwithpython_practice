import urllib.request
import xml.etree.ElementTree
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input("Enter url: ")
xml_data=urllib.request.urlopen(url,context=ctx).read()
t=xml.etree.ElementTree.fromstring(xml_data)
numbers=t.findall('.//count')
answer=0
for number in numbers:
    answer+=int(number.text)
print(answer)

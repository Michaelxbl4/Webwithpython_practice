import socket
import xml.etree.ElementTree
url=input("Enter url: ")
url_=url.split('/')[2]
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((url_,80))
#cmd=('GET '+url+' HTTP/1.0\r\n\r\n').encode() direct ip access banned by cloudfare as it thinks we might be trying to access serverso for security reasons we must tell the host name we are trying to access
cmd = ('GET ' + url + ' HTTP/1.0\r\nHost: ' + url_ + '\r\n\r\n').encode()
mysock.send(cmd)
xml_data=b""
while True:
    data=mysock.recv(1000)
    xml_data+=data
    if len(data) == 0:
        break
xml_data=(xml_data.decode()).split('\r\n\r\n')[1]
print(xml_data)
t=xml.etree.ElementTree.fromstring(xml_data)
numbers=t.findall('.//count')
answer=0
for number in numbers:
    answer+=int(number.text)
print(answer)

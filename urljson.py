import urllib.request, json, ssl
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
location=input("Input location: ")
location=location.strip()
parms = dict()
parms['q'] = location
url = serviceurl + urllib.parse.urlencode(parms)
print("Retrieving",url)
data=urllib.request.urlopen(url,context=ctx).read().decode()
print("Retrieved "+str(len(data))+" characters")
data=json.loads(data)
print("Plus Code",data['features'][0]['properties']['plus_code'])
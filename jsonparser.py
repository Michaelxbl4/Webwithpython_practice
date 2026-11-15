import urllib.request, json, ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input("Enter url: ")
json_dsta=json.loads(urllib.request.urlopen(url,context=ctx).read())
answer=0
for comment in json_dsta['comments']:
    answer+=comment['count']
print(answer)
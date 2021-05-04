
import json
import ssl
import urllib.request, urllib.parse, urllib.error

count = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "http://py4e-data.dr-chuck.net/comments_1220846.json"
data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)
for item in info["comments"]:
	number = int(item["count"])
	count = count + number
print(count)

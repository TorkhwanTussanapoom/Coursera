import json
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
data = input("Enter:")
html = urllib.request.urlopen(data, context=ctx).read()
info = json.loads(html)
for sub in info:
    for key in sub:
        sub[key] = int(sub[key])
for item in info:
    print('count', item['count'])

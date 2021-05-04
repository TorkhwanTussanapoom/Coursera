import json
import urllib.request,urllib.parse, urllib.error
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input("Location - ")
adress = input("Address - ")

addressandkey = urllib.parse.urlencode({'address':adress,'key':42})

try :
    data_read = urllib.request.urlopen(link + addressandkey, context=ctx).read()
    data = data_read.decode()
    js = json.loads(data)
    place_id = js['results'][0]['place_id']
    print("Place id", place_id)
except:
    print("--------")

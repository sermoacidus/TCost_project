import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


url = '''https://api.jde.ru/vD/calculator/price?from=1125899906842658&to=112589990
6842673&weight=25&width=1&volume=0,02&type=1'''

print('Retrieving', url, sep=' ----->>>  ')

#requesting data
urlop = urllib.request.urlopen(url)
data = urlop.read().decode()
print('Retrieved', len(data), 'characters')
print(data,type(data))

#converting data to .dict
try:
    js = json.loads(data)
except:
    js = None
print(js,type(js))

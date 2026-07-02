import requests

# r = requests.get('https://xkcd.com/353/')
# print(r)
# <Response [200]>

# print(dir(r))
# ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

# print(help(r))

# print(r.text)
# <!DOCTYPE html>
# <html>
# ...
# </html>

# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.content)
# oA1C\xccV\xe2Y\xacU,\x1f*\xb5q\xc5\xa7n\xa1/<2\xed\xf5\x19\x9f\xd2\xcb\x81\xcf\x95N\xb3\xad\xb2\x0f<\xb2\xe8\x92Y\\\xa9\x99yLv1\xb8,\x84\xd0\xb3\xda\x9b\x8bO\xf3\x87\x86\xe2\xbf&Xn\xc3\xbdagI\xad\xdf\xe3\xa5\'\  ...

# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# print(r.status_code)
# print(r.ok)
# print(r.headers)
# 200
# True
# {'Connection': 'keep-alive', 'Content-Length': '90835', 'Server': 'nginx', 'Content-Type': 'image/png', 'Last-Modified': 'Mon, 01 Feb 2010 13:07:49 GMT', 'ETag': '"4b66d225-162d3"', 'Access-Control-Allow-Origin': '*', 'Accept-Ranges': 'bytes', 'Age': '424', 'Date': 'Sat, 27 Jun 2026 00:30:59 GMT', 'Via': '1.1 varnish', 'X-Served-By': 'cache-ccu830046-CCU', 'X-Cache': 'HIT', 'X-Cache-Hits': '0', 'X-Timer': 'S1782520260.539035,VS0,VE1'}

# in generally we pass params with url like ?p1=o1&p2=02
# like that we dont ened to hard code like this
# r = requests.get("https://httpbin.org/get?page=2&count=25")
# print(r.url)
# print(r.text)
# https://httpbin.org/get?page=2&count=25
# {
#   "args": {
#     "count": "25", 
#     "page": "2"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.32.5", 
#     "X-Amzn-Trace-Id": "Root=1-6a3f1ae7-06380c1a53d5536172bd4bef"
#   }, 
#   "origin": "49.204.236.140", 
#   "url": "https://httpbin.org/get?page=2&count=25"
# }
# we will create payload dict and pass it as params
# payload = {'page':2, 'count':25}
# r = requests.get("https://httpbin.org/get", params=payload)
# print(r.url)
# print(r.text)
# https://httpbin.org/get?page=2&count=25
# {
#   "args": {
#     "count": "25", 
#     "page": "2"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.32.5", 
#     "X-Amzn-Trace-Id": "Root=1-6a3f1ae8-1ce7d5d11fbfa80368cf12f9"
#   }, 
#   "origin": "49.204.236.140", 
#   "url": "https://httpbin.org/get?page=2&count=25"
# }

# now so far we have done get reqeusts
# now to do post use requests.post(url, data=payload)

# payload = {'user': 'corey', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text)
# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {
#     "password": "testing", 
#     "user": "corey"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Content-Length": "27", 
#     "Content-Type": "application/x-www-form-urlencoded", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.32.5", 
#     "X-Amzn-Trace-Id": "Root=1-6a3f1c00-219df197707ee8d37f75e551"
#   }, 
#   "json": null, 
#   "origin": "49.204.236.140", 
#   "url": "https://httpbin.org/post"
# }
# most fo them are json we can convert to dict using .json() and access corresponding parts

# r_dict = r.json()
# print(r_dict['form'])
# {'password': 'testing', 'user': 'corey'}

# r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
# print(r.text)
# {
#   "authenticated": true, 
#   "user": "corey"
# }

# we can set timeout to return error when response not get wwithin time mentioed
r = requests.get('https://httpbin.org/delay/2', timeout=3)
print(r.text)
# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.32.5", 
#     "X-Amzn-Trace-Id": "Root=1-6a3f1ef2-241465a9190188c23ac69b5d"
#   }, 
#   "origin": "49.204.236.140", 
#   "url": "https://httpbin.org/delay/2"
# }

# lets say we mentioned less timeout than actual response time then get error
# r = requests.get('https://httpbin.org/delay/6', timeout=3)
# print(r.text)
# requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='httpbin.org', port=443): Read timed out. (read timeout=3)
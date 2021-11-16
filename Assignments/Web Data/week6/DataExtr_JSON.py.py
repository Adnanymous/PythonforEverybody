''' Read JSON data from http://py4e-data.dr-chuck.net/comments_42.json then parse and extract the comment counts
and compute the sum of numbers
'''

import urllib.request, urllib.parse, urllib.error
import ssl
import json

sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
info = json.loads(data)

for item in info['comments']:   #The JSON data is a dictictionary with two objects ('notes' and 'comments') we only care about 'comments'
    count = int(item['count'])
    sum = count + sum
print(sum)

'''Read XML data from a URL using urllib, parse and extract the comment counts from the XML data and compute the sum of the numbers in the file
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

sum = 0
url = 'http://py4e-data.dr-chuck.net/comments_1396942.xml'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

comment = ET.fromstring(data)
counts = comment.findall('.//count')


for item in counts:
    sum = sum + int(item.text)
print(sum)

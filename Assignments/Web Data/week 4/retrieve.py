'''Retrieve a link from a particular position from the list, follow that link and repeat the process a number of times
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = input('Enter count: ')
count = int(count)
pos = input('Enter position: ')
pos = int(pos)

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

for i in range(0, count+1):                                 #Looping x count times
    print('Retrieving', url)
    tags = soup('a')
    url = str(tags[pos - 1].get('href', None))              #Assigning the new url as the string in position (pos - 1) of the list
    html = urllib.request.urlopen(url, context=ctx).read()  #Going to the new url
    soup = BeautifulSoup(html, 'html.parser')               #The new html file is ready to be read

''' Find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers
by pulling out the text content of the span tag, convert them to integers and add them up
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    x = str(tag)
    y = re.findall('comments">(.+)<',x) # pulls out the numbers
    for i in range(0, len(y)):          #turns the numbers into integers
        y[i] = int(y[i])
        sum = sum + y[i]                #sums the numbers up
print(sum)

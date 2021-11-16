'''Read through and parse a file with text and numbers, extract the numbers in the file
and compute the sum of the numbers
'''

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1396938.txt"
handle = open(name)

import re
sum = 0

for line in handle:                         #Read through lines
    x = re.findall('[0-9]+', line)          #Find any number of digits in lines
    if len(x) < 1:                          #Skip blank lines
        continue
    for i in range(0, len(x)):              #Convert the list of strings into integers
        x[i] = int(x[i])
        sum = sum + x[i]                    #sum up the numbers
print(sum)

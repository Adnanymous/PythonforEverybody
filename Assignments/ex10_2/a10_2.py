'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using
a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograde
r does not have support for the sorted() function.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts=dict()
answ = list()

for line in handle:
    words = line.split()                                #Splits lines into words
    if len(words) < 1 or words[0] != "From":            #Picks lines that start with "From", and are not blank
        continue
    hr = words[5].split(':')                            #Splits time into hours, minutes, seconds

    counts[hr[0]] = counts.get(hr[0], 0) +1             #Increase count for each hour

for h, c in counts.items():
    toup = (h, c)
    answ.append(toup)                                   #appends touples to the list

answ = sorted(answ)                                     #Sorts list by hour

for h, c in answ:
    print(h, c)                                         #print counts sorted by hour

#print(sorted([(k,v) for k, v in counts.items()]))

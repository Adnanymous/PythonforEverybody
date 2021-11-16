#Top 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#We can use this:
lst = list()
for key, val in counts.items():
   newtup = (val, key)
   lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst [:10]:
   print(key, val)

#Alternatively we can use this:
print(sorted([(v,k) for k, v in counts.items()]))


#Touples look exactly like a list except they use () instead of []
#Dictionaries use {}
#Lists are mutable, strongs and touples are not.

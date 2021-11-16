#Sorting by value not key:
c = {'a':10, 'b':1. 'c':22}
tmp = list()
for k, v om c.items():
    tmp.append((v, k))

tmp = sorted(tmp, reverse=True)

fname = input("Enter file name: ")
fh = open(fname)
for itr in fh:
    itr = itr.upper()
    itr = itr.strip()
    print(itr)

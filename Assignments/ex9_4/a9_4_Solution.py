#I don't know why this code works!
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.split()
    #Guardian Phrase - Prevents syntax error due to empty lines and looks only at lines that starts with From:
    if len(line) < 1 or line[0] != 'From:':
        continue
    for word in line:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
print(word, counts[word])

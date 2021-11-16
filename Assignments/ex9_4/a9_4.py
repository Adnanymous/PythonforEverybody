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
    #Looks only into the second words of the lines that starts with From:
    counts[line[1]] = counts.get(line[1], 0) +1

max_word = None
max_count = None
#Moves the count into max_count if no count is available, or the count is larger than max_count
for word,count in counts.items():
    if max_count is None or count > max_count:
        max_word = word
        max_count = count
print(max_word, max_count)

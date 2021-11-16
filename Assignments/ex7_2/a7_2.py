fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    text = line.find('0')
    num = float(line[text:])
    total = total + num
    count = count + 1

print('Average spam confidence:', total/count)

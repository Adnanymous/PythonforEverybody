text = "X-DSPAM-Confidence:    0.8475"
num = text.find('0')
number = text[num:]
n = float(number)
print(n)

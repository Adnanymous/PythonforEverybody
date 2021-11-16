xhr = input('Enter hours: ')
xrt = input('Enter rate: ')
whr = float(xhr)
wrt = float(xrt)
if whr <= 40:
    wpay = whr *wrt
elif whr > 40:
    wpay = (40 * wrt) + (whr - 40) * 1.5* wrt
print(wpay)

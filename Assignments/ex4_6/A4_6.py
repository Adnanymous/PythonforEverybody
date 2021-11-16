def computepay(h,r):
    if h <= 40:
        p = h *r
    elif h > 40:
        p = (40 * r) + (h - 40) * 1.5* r
    return p

hr = input('Enter hours: ')
rt = input('Enter rate: ')
fhr = float(hr)
frt = float(rt)
pay =computepay(fhr, frt)
print ("Pay", pay)

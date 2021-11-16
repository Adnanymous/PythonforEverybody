largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numbr = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = numbr
        largest = numbr
    elif smallest > numbr:
        smallest = numbr
    elif largest < numbr:
        largest = numbr

print("Maximum is", largest)
print("Minimum is", smallest)

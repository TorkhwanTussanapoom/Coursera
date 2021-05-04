largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try: float(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = num
    elif smallest is None:
        smallest = num
    elif largest > num:
        largest = num
    elif num < smallest:
        smallest = num
print("Maximum is", largest)
print("Minimum is", smallest)

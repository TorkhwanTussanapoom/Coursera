hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
if hrs > 40:
    pay1 = 40 * rate #420?
    hrs2 = (hrs - 40)
    rate2 = rate * 1.5
    pay2 = hrs2 * rate2
    print(pay1+pay2)
else:
    print(hrs * rate)

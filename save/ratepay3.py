def computepay(h,r):
    if h > 40 :
        return (40 * rate) + ((hrs - 40) * (rate * 1.5))
    else:
        return hrs * rate
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
rate = float(rate)
hrs = float(hrs)
p = computepay(hrs,rate)
print("Pay",p)

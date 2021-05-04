fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x = line.find(":")
    y = float(line[x+1:])
    total = total + y
    count = count + 1
total2 = total / count
print("Average spam confidence:" , total2)

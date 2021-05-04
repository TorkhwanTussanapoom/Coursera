fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
     line = line.rstrip()
     line = line.split()
     for words in line:
          if words in lst:
                continue
          else: lst.append(words)
lst.sort()
print(lst)

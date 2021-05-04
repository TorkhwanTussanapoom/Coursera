name = input("Enter file:")
handle = open(name)
counts = dict()
x = list()
for lines in handle:
    if not lines.startswith('From') : continue
    if lines.startswith('From:'): continue
    else:
        lines = lines.split()
        lines = lines[5]
        lines = lines[:2]
        counts[lines] = counts.get(lines,0) + 1
x = list()
for k,v in counts.items():
    x.append((k,v))
x.sort()
for k,v in x:
     print(k,v)

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for lines in handle:
    if not lines.startswith('From') : continue
    if lines.startswith('From:'): continue
    else:
        lines = lines.split()
        lines = lines[1]
        counts[lines] = counts.get(lines,0) + 1
    bigcount = None
    bigword = None
    for word,count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
print(bigword,bigcount)

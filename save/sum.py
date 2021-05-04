
import re
sum=0
for lines in open("""regex_sum_1220841.txt""",'r'):
    line = re.findall('[0-9]+', lines)
    for x in line:
        sum = sum+int(x)
print(sum)

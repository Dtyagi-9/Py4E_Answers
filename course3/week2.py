import re

file = input("enter the file name ")
fh = open(file)
ls= list()
for line in fh:
	line = line.strip()
	num = re.findall('[0-9]+' ,line)
	if len(num) == 0:
		continue
	for n in num:
		x=int(n)
		ls.append(x)
print(sum(ls))

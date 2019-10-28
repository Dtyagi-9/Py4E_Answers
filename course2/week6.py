name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
ls=dict()
for line in handle:
    line.rstrip()
    if line.startswith('From'):
        words=line.split()
        if len(words)>6:
            time=words[5]
            hrs=time.split(':')
            hr=hrs[0]
            ls[hr]=ls.get(hr,0)+1
ls=sorted(ls.items())
for x,y in ls:
    print(x,y)
#extraction of string can be done using other possibilities as well

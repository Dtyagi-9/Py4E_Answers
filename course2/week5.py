name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh=open(name)
count=dict()
for line in fh:
    if line.startswith('From'):
        line=line.rstrip()
        words=line.split(' ')
        if len(words)>4:
            name=words[1]
            count[name]=count.get(name,0)+1
maxname=None
maxnum=None
for i in count:
    if maxname==None:
        maxname=i
        maxnum=count[i]
    if count[i]>maxnum:
        maxname=i
        maxnum=count[i]
print(maxname,maxnum)
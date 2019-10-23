fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find(' ')
    num=line[pos+1:]
    num=float(num)
    total+=num
    count+=1
    
print('Average spam confidence:',total/count)
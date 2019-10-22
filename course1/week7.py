l = None
s = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num=int(num)
        if l==None :
            l=num
        if s==None :
            s=num
        if num>l :
            l=num
        if num<s :
            s=num
    except:
        print('Invalid input')
        continue
        
print("Maximum is", l)
print("Minimum is", s)
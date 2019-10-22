hrs=float(input('Enter the hours:'))
rate=float(input('Enter the rate:'))
def computepay(h,r):
    if h<=40:
        pay=h*r
    else :
        h=h-40
        pay=40*r+(h*r*1.5)
    return pay
p=computepay(hrs,rate)
print(p)
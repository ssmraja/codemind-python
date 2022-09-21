N=int(input())
rev=0
t=N
while N>0:
    r=N%10
    rev=rev*10+r
    N=N//10
if t==rev:
    print("True")
else:
    print("False")
    
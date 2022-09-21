N=int(input())
rev=0
while N>0:
    r=N%10
    rev=rev*10+r
    N=N//10
print(rev)    
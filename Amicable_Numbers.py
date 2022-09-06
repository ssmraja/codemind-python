n=int(input())
m=int(input())
count=0
count1=0
for i in range(1,n):
    if n%i==0:
        count+=i
for b in range(1,m):
    if m%b==0:
        count1+=b
if count==m and count1==n:
    print("Amicable")
else:
    print("Not Amicable")
        
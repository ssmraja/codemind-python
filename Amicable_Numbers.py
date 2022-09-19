a=int(input())
b=int(input())
sum=0
sum1=0
for i in range(1,a):
    if a%i==0:
        sum+=i
for i in range(1,b):
    if b%i==0:
        sum1+=0
if sum==b or sum1==a:
    print("Amicable")
else:
    print("Not Amicable")
        
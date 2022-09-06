N=int(input())
count=0
for i in range(1,N):
    if N%i==0:
        count+=i
if count>N:
    print("True")
else:
    print("False")
##Task 6_1
n=int(input())
s=0
for i in range(0,n):
    a=int(input())
    if a==0:
        s+=1
print(s)

##Task 6_2
x=0
s=0
while x<1 or x>=2e9: 
    x=int(input())
for i in range(1,x+1):
    if x%i == 0:
        s+=1
print(s)

##Task 6_2
a=int(input())
b=int(input())
if a>b:
    while a>b: 
        b=int(input())
    print(b,a)
for i in range(a,b+1):
    if i%2==0:
        print(i,end=' ')
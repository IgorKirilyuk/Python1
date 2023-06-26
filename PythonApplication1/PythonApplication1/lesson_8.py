##Task 8_1
l=[]
n=0
while n<1 or n>10000:
    n=int(input())
for i in range(n):
    a=0
    while (a<-10e5 or a>10e5 or a==0) :
        a=int(input())
    l.append(a)
l.reverse()
print(l)

##Task 8_2
n=0
l=[]
while n<1 or n>100000:
    n=int(input())
print(f"Vvedite cherz probel {n} chisel.")
l=list(map(int,input().split()))
l.insert(0,l.pop())
print(l[:n])

##Task 8_3
min_=0
m=0
n=0
l=[]
print("max massa?")
while m<1 or m>10e6:
    m=int(input())
print("kol-vo chel?")
while n<1 or n>100:
    n=int(input())
print(f"massa dlya {n} chel")
for i in range(n):
    l.append(int(input()))
    l.sort()
    l.reverse()
while len(l)>0:
    cm=0
    lt=[]
    for i in range(len(l)):
        if cm+l[i]<=m:
            cm+=l[i]
        else:
            lt.append(l[i])
    if cm>0: min_+=1
    l=lt.copy()
print(f"vsego lodok {min_}")
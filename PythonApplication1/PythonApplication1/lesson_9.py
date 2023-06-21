#Task 9_1
n=0
nl=0
f=0
while n<1 or n>100000:
    n=int(input())
while nl>n or nl<1 or f==1:
    f=0
    print(f"Vvedite cherz probel {n} chisel.")
    l=list(map(int,input().split()))
    nl=len(l)
    l.sort()
    if len(l) > 0:
        if l[-1] > 2*10e9 or l[0] < -2*10e9:
            f=1
tl = set(l)
print(len(tl))

##Task 9_2
tmp1 = set()
tmp2 = set()
tmp3 = set()
print(f"Vvedite kol-vo tmp1 <100000.")
n=0
while n<1 or n>=100000:
    n=int(input())
print(f"Vvedite tmp1")
for i in range(n):
    tmp1.add(int(input()))
print(f"Vvedite kol-vo tmp2 <100000.")
n=0
while n<1 or n>=100000:
    n=int(input())
print(f"Vvedite tmp2")
for i in range(n):
    tmp2.add(int(input()))
tmp3=tmp2.intersection(tmp1)
print(len(tmp3))

##Task 9_3
tmp=set()
l=list(map(int,input().split()))
for i in l:
    if i in tmp:
        print(f"{i} YES")
    else:
        print(f"{i} NO")
        tmp.add(i)
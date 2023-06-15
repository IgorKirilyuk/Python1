

##Task 5_1
i = int(input())
if i == 0:
    print('nulevoe chislo')
    exit(0)
elif i%2 == 0 and i > 0:
    print ('polojitelnoe chetnoe chislo')
elif i%2 == 0 and i < 0:
    print('otrizzatelnoe chetnoe chislo')
else: print('nechetnoe chislo')

##Task 5_2
i = str(input())
ni_ = len(i)
g_ = 'aei'
ng_ = len(g_)
s_ = 'tpn'
ns_ = len(s_)
gs_ = 0
ss_ = 0

n=0
while n<ng_:
    ch = g_[n]
    n1 = 0
    s1 = 0
    while n1 < ni_:
        if i[n1] == ch:
            s1 += 1
        n1 += 1
    if s1 == 0:
        print(ch, 'false')
    else:
        print(ch, s1)
    gs_ += s1
    n += 1
print ('vsego glasnblh:',gs_)
 
n=0
while n<ns_:
    ch = s_[n]
    n1 = 0
    s1 = 0
    while n1 < ni_:
        if i[n1] == ch:
            s1 += 1
        n1 += 1
    if s1 == 0:
        print(ch, 'false')
    else:
        print(ch, s1)
    ss_ += s1
    n += 1
print ('vsego soglasnblh:',ss_)

##Task 5_3

min_ = int(input())
mik_ = int(input())
ivan_ = int(input())

if mik_ + ivan_ < min_:
    print (0)
elif  mik_ >= min_ and ivan_ >= min_:
    print (2)
elif  mik_ >= min_ and ivan_ < min_:
    print ('Mike')
elif  mik_ < min_ and ivan_ >= min_:
    print ('Ivan')
elif  mik_ + ivan_ >= min_:
    print (1)
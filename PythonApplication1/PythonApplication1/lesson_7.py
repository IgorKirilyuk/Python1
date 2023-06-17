##Task 7_1
s=str('')
while len(s)<1 or len(s)>1000:
    s = str(input())
if len(s) == 1:
    print('yes')
    exit()
n=len(s)//2
s1=s[:n]
s2=s[len(s)-1:len(s)-1-n:-1]
if s1==s2:
    print('yes')
else:
    print('no')

##Task 7_2
s=str('')
while len(s)<1 or len(s)>1000:
    s = str(input())
while s.find('  ') > -1:
    s = s.replace('  ',' ')
print(s)
#### LESS 13
###dvumernble

##Task 13_1
import random
x=0
y=0
while x<=0:
    x=int(input('Vvedite razmer matix po X: '))
while y<=0:
    y=int(input('Vvedite razmer matix po Y: '))

matrix_1=[[0 for i in range(x)]for i in range(y)]
matrix_2=[[0 for i in range(x)]for i in range(y)]
matrix_res=[[0 for i in range(x)]for i in range(y)]

for i in range(y):
    for j in range(x):
        matrix_1[i][j]=random.randrange(-100,100)
print(matrix_1)
for i in range(y):
    for j in range(x):
        matrix_2[i][j]=random.randrange(-100,100)
print(matrix_2)
for i in range(y):
    for j in range(x):
        matrix_res[i][j]=matrix_1[i][j]+matrix_2[i][j]
print(matrix_res)
#### LESS 14
###########recursiya
###Task 14_1
def rec(x):
    if x>len(my_list)-1:
        return
    print (my_list[x])
    rec(x+1)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
a=0
rec(a)
print('konezz spiska')

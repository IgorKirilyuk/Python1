### LESS 10

##Task 10_1
def inp_pet():
    print('input name pet:')
    name_=''
    while len(name_)<1:
        name_=str(input())
    pets[name_]=dict()
    print(f'input type pet {name_}:')
    type_=''
    while len(type_)<1:
        type_=str(input())
    pets[name_]['type']=type_
    print(f'input age pet {name_}:')
    age_=-1
    while age_<0 or age_>=1000:
            age_=int(input())
    pets[name_]['age']=age_
    print(f'input owner pet {name_}:')
    owner_=''
    while len(owner_)<1:
        owner_=str(input())
    pets[name_]['owner']=owner_

def age_list(age_):
    let_=[5,6,7,8,9,0]
    god_=[1]
    goda_=[2,3,4]
    if age_>10 and age_<20:
        age_l='let'
    elif age_%10 in let_:
        age_l='let'
    elif age_%10 in god_:
        age_l='god'
    elif age_%10 in goda_:
        age_l='goda'
    else:
        age_l='err'
    return(f'{age_} {age_l}')

pets=dict()
print('input qnt pets')
n=0
while n<1:
    n=int(input())
for i in range(n):
    inp_pet()
for i in pets:
    print(f"Eto {pets[i]['type']}, po klichke {i}. Vozrast {age_list(pets[i]['age'])}. Imya vladelzza: {pets[i]['owner']}.")


##Task 10_2
temp_=dict()
for i in range(10,-5,-1):
    temp_[i]=i**i
print (temp_)
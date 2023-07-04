### LESS 11

##Task 11_1
def gf_ (a):
        n=1
        for i in range(1,a+1):
            n*=i
        return(n)

a=0
f_=[]
while a<1:
    a=int(input('vvedite zzelo chislo: '))
a=gf_(a)
for b in range(a,0,-1):
    f_.append(gf_(b))
print(f_)


##Task 11_2
def get_pet():
    a=0
    a=int(input('index pet?: '))
    if a in pets: return(a)
    else: return(0)

def get_suffix(age_):
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

def create():
    if len(pets)>0:
        last_ = collections.deque(pets, maxlen=1)[0]
    else: last_ = 0
    name_='' #####
    while len(name_)<1:
        name_=str(input('input name pet: '))
    pets[last_+1]=dict()
    tmp_=dict()
    type_='' #####
    while len(type_)<1:
        type_=str(input(f'input type pet {name_}: '))
    tmp_['type']=type_
    age_=-1 #####-1
    while age_<0 or age_>=1000:
            age_=int(input(f'input age pet {name_}: '))
    tmp_['age']=age_
    owner_='' #####
    while len(owner_)<1:
        owner_=str(input(f'input owner pet {name_}: '))
    tmp_['owner']=owner_
    pets[last_+1][name_]=tmp_
    print(f"Dobavlen {type_}, po klichke {name_}.")

def delete():
    a=get_pet()
    if a>0:
        print(f"Udalen pet #{a}.")
        pets.pop(a)
    else: print('Nevernbly index')

def read():
    a=get_pet()
    if a > 0:
        for i in pets[a]:
            print(f"Eto {pets[a][i]['type']}, po klichke {i}. Vozrast {get_suffix(pets[a][i]['age'])}. Imya vladelzza: {pets[a][i]['owner']}.")
    else: print('Nevernbly index')

def update():
    a=get_pet()
    if a>0:
        for i in pets[a]:
            key_=input(f'vvedite odin iz klyuchey ({pets[a][i].keys()}): ')
            if key_ in pets[a][i]:
                if type(pets[a][i][key_]) != int: val_=input('vvedite znachenie: ')
                else: val_=input('vvedite znachenie: ')
                pets[a][i][key_]=val_
                print(f"obnovlen key {key_}: {val_}.")
            else: print("err") 

import collections
command = 'start'
pets = dict()

while command != 'stop':
    command=input('Vvedite commandu (create;read;delete;update;stop): ')
    if command == 'create':
        create()
    if command == 'delete':
        delete()
    if command == 'read':
        read()
    if command == 'update':
        update()
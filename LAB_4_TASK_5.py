#TASK 5
divided={'Tony':41,'Rhodey':43,'Nat':35}
we_fall={'Steve':39,'Clint':35,'Wanda':28}

#Part -a-
print('\nPART A\n')
united_we_stand={}

for i in divided:
    united_we_stand[i]=divided[i]

for i in we_fall:
    united_we_stand[i]=we_fall[i]

for i in united_we_stand:
    print(f'{i} {united_we_stand[i]}')


#Part -b-
print('\nPART B')
united_we_stand.pop('Nat')
print('Nat is removed: ',united_we_stand)

#Part -c-
print('\nPART C')
def sortByKey(d:dict):
    l=list()
    for i in d:
        l.append(i)
    l.sort()
    new_d={}
    for i in l:
        new_d[i]=d[i]
    return new_d

sorted_united_we_stand=sortByKey(united_we_stand)
print('Sorted by the keys',sorted_united_we_stand)

#Part -d-
print('\nPART D')
def findMax(d:dict):
    max=0
    key=''
    l=[]
    for i in d:
        l.append(d[i])
    l.sort()
    max=l[len(l)-1]
    for i in d:
        if d[i]==max:
            key=i
            break
    return key

def findMin(d:dict):
    min=0
    key=''
    l=[]
    for i in d:
        l.append(d[i])
    l.sort()
    min=l[0]
    for i in d:
        if d[i]==min:
            key=i
            break
    return key

print(f'Max Aged Hero => Name: {findMax(united_we_stand)} Age: {united_we_stand[findMax(united_we_stand)]}')
print(f'\nmin Aged Hero => Name: {findMin(united_we_stand)} Age: {united_we_stand[findMin(united_we_stand)]}')


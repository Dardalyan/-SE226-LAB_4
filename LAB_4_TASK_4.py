#TASK 4

#Part -a-
print('\nPART A')
sample ={}

for i in range(1,31):
    sample[i] = (i-1)*(i+1)

print('Dictionary:',sample,'\n')

#Part -b-
print('\nPART B')
for i in range(1,31):
    print(f'Key:{i} Value: {sample[i]}')

#Part -c-
print('\nPART C')
sum =0
for i in range(1,31):
    sum+=sample[i]
print(f'\nSum : {sum}')

#Part -d-
print('\nPART D')
status=True
print('Please enter a number to delete a value from the dictionary ...')
while(status):
    num = int(input())
    try:
        sample.pop(num)
        status=False
    except:
        print('Please try again you have entered a invalid key !')

print(sample)
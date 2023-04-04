from words import words # !! importing words from words.py file !!

#TASK 1
number1=int(input('Please enter 2 numbers between (1) and (9999) which the first one must be greater than the second one...'))
number2=int(input())

if number2>number1:
    while (True):
        print('You have entered the second number as a greater than the first one please try again...')
        number1 = int(input('Please enter 2 numbers between (1) and (9999) which the first one is greater than the second one...'))
        number2 = int(input())
        if number1 > number2:
            break
        else:
            continue

selection=[words[number1],words[number2]]
for i in range(0,len(selection)):
    print(f'Chosen Word {i+1} :',selection[i])
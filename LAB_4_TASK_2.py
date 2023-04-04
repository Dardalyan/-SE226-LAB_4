from words import words # !! importing words from words.py file !!
from random import randint

#TASK 2

def makePassword(someList:list):
    word = ''
    for i in someList:
        word += i
    return word[::-1]

user_number=int(input('Please enter a number between 3 and 7'))
acceptable_range=[3,4,5,6,7] # accepted numbers from the user

if user_number not in acceptable_range:
    while(True):
        print('You have entered a number out of range please try again...')
        user_number=int(input())
        if user_number>=3 and user_number<=7:
            break
        else:
            continue

random_words=[]
for i in range(0,user_number):
    random_words.append(words[randint(0,999)])


password = makePassword(random_words)
print(password)





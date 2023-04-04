from words import words # !! importing words from words.py file !!
from random import randint

#TASK 3

def makePassword(someList:list):
    word = ''
    for i in someList:
        word += i
    return word[::-1]

acceptable_range=[3,4,5,6,7] # accepted numbers from the user



shorter = set()
longer  = set()

for i in range(8):
    print(f'For the password {i+1}:')
    user_number = int(input('Please enter a number between 3 and 7\n'))

    if user_number not in acceptable_range:
        while (True):
            print('You have entered a number out of range please try again...')
            user_number = int(input())
            if user_number >= 3 and user_number <= 7:
                break
            else:
                continue

    if user_number >=5:
        random_words = []
        for i in range(0, user_number):
            random_words.append(words[randint(0, 999)])
        password = makePassword(random_words)
        longer.add(password)
    else:
        random_words = []
        for i in range(0, user_number):
            random_words.append(words[randint(0, 999)])
        password = makePassword(random_words)
        shorter.add(password)




print('Longer Set :',longer,'\n')
print('Shorter Set :',shorter,'\n')

combined = longer.union(shorter)
print('Combined Set: ',combined)
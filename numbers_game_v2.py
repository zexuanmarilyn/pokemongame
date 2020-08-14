#build a numbers guessing game, between 1 - 100
#computer will randomly select number
#user to guess number. if correct, print congrats message
#if wrong, to hint user if number is higher or lower

import random


def game_setup():
    list_of_numbers=[]
    for number in range(1,101):
        list_of_numbers.append(number)
    

    random_number=random.sample(list_of_numbers,1)
    global comp_gen_num
    comp_gen_num=int(random_number[0])
    return comp_gen_num

print(game_setup())


#question - how to prevent first part of code from rerunning again?

#2nd portion - let user choose a number and return whether its correct
user_number_choice=int(input("Pick a number:"))
while user_number_choice != comp_gen_num:
    if user_number_choice < comp_gen_num:
        message="Number chosen is lower than actual"
    else:
        message="Number chosen is higher than actual"
    print(message)
    user_number_choice=int(input("Pick a number:")

if user_number_choice == comp_gen_num:
     message ="Congratulations, you have won"
print(message)

# building a simple number guessing game
# rules: the computer will randomly select a number between 1 - 100. The aim of the game is for the player to guess the number as quickly as possible. 
# The program will hint the user if the selected number is higher or lower than the number the player guessed.


import random


# code to generate a random number
def game_setup():
    list_of_numbers=[]
    for number in range(1,101):
        list_of_numbers.append(number)
    

    random_number=random.sample(list_of_numbers,1)
    global comp_gen_num
    comp_gen_num=int(random_number[0])
    return comp_gen_num
comp_gen_num=game_setup()





#allow user to choose a number and return response as to whether the player has guessed the correct number. If wrong number, to hint whether actual number is higher or lower.
user_number_choice=int(input("Pick a number:"))
lowered_limit= 1
higher_limit=100
while user_number_choice != comp_gen_num:
    if user_number_choice < lowered_limit:
        message="Number not within range. Please pick a higher number"
    elif user_number_choice > higher_limit:
        message= "Number not within range. Please pick a lower number"
    elif user_number_choice < comp_gen_num:
        message="Number chosen is lower than actual"
        lowered_limit=user_number_choice
    else:
        message="Number chosen is higher than actual"
        higher_limit=user_number_choice
    print(message)
    user_number_choice=int(input(("Pick a number between {} to {}:").format(lowered_limit, higher_limit)))


if user_number_choice == comp_gen_num:
     message ="Congratulations, you have won, the number is "+str(comp_gen_num)
print(message)

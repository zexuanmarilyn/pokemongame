#build a numbers guessing game, between 1 - 100
#computer will randomly select number
#user to guess number. if correct, print congrats message
#if wrong, to hint user if number is higher or lower

from random import sample

list_of_numbers=[]
for number in range(1,101):
    list_of_numbers.append(number)
print(list_of_numbers)
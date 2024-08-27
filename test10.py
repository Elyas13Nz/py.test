import random

number = random.randint(1, 10)
player_name = input("Hello, What's your name?")
number_of_hads = 0

print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_hads <= 4:
    hads = int(input())
    number_of_hads += 1

    if hads < number:
        print('Your hads is too low')

    if hads > number:
        print('Your hads is too high')

    if hads == number: break
        

if hads == number:
    print('You hads the number in ' + str(number_of_hads) + ' tries!')

else:
    print('You did not hads the number, The number was ' + str(number))

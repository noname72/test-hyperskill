from random import choice


options = ['rock', 'paper', 'scissors']


do_game = True

while do_game:
    user_option = input()
    random_option = choice(options)
    if user_option == random_option:
        print(f'There is a draw ({user_option})')
    elif user_option == 'rock' and random_option == 'paper':
        print(f'Sorry, but computer chose {random_option}')
    elif user_option == 'paper' and random_option == 'scissors':
        print(f'Sorry, but computer chose {random_option}')
    elif user_option == 'scissors' and random_option == 'rock':
        print(f'Sorry, but computer chose {random_option}')
    elif user_option == '!exit':
        print('Bye!')
        do_game = False
    elif user_option not in options:
        print('Invalid input')
    else:
        print(f'Well done. Computer chose {random_option} and failed')
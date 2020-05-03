from random import choice

options_default = ['rock', 'paper', 'scissors']
options_extended = ['rock', 'fire', 'scissors', 'snake', 'human',
                    'tree', 'wolf', 'sponge', 'paper', 'air',
                    'water', 'dragon', 'devil', 'lighting', 'gun']
user_score = 0
run_game = True


def beaten_list(option):
    index = options_extended.index(option)
    _temp = options_extended.remove(option)


while run_game:
    user_name = input('Enter your name:')
    print('Hello,' + user_name)
    f = open('rating.txt', 'r')
    for user_line in f:
        if user_name in user_line:
            score = user_line.split(' ')
            user_score = int(score[1])
    user_option = input()
    random_option = choice(options_default)
    if user_option == random_option:
        print(f'There is a draw ({user_option})')
        user_score += 50
    elif user_option == 'rock' and random_option == 'paper':
        print(f'Sorry, but computer chose {random_option}')
    elif user_option == 'paper' and random_option == 'scissors':
        print(f'Sorry, but computer chose {random_option}')
    elif user_option == 'scissors' and random_option == 'rock':
        print(f'Sorry, but computer chose {random_option}')
    elif user_option == '!rating':
        print('Your rating:', user_score)
    elif user_option == '!exit':
        print('Bye!')
        run_game = False
    elif user_option not in options_default:
        print('Invalid input')
    else:
        print(f'Well done. Computer chose {random_option} and failed')
        user_score += 100

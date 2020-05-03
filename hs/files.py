options = ['rock', 'gun', 'lightning', 'devil', 'dragon',
           'water', 'air', 'paper', 'sponge', 'wolf',
           'tree', 'human', 'snake', 'scissors', 'fire']


def option_beaten_by(option):
    idx = options.index(option)
    if idx > 7:
        if len(options) - idx >= 7:
            _beats = options[idx - 8::-1]
        else:
            _beats = options[-15 + idx:0:-1]
    else:
        _beats = options[idx + 1:idx + 8:1]
    print(f'{option} beaten by {_beats}')


for i in range(0, 16):
    print(option_beaten_by(options[i]))

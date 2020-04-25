import random
import string


class Hangman:
    def __init__(self):
        self.word_list = ['python', 'java', 'kotlin', 'javascript']
        self.random_word = random.choice(self.word_list)
        self.uncovered_word = len(self.random_word) * '-'
        self.tries_left = 8
        self.uncovered_list = []
        self.typed_letters = []
        print("H A N G M A N")

    def uncover_letters(self, letter):
        self.uncovered_word = ''
        for let in self.random_word:
            if let == letter:
                self.uncovered_word += let
                self.uncovered_list.append(let)
            elif let in self.uncovered_list:
                self.uncovered_word += let
            else:
                self.uncovered_word += '-'

        return self.uncovered_word

    def start_game(self):
        while self.tries_left >= 1:
            print('\n' + self.uncovered_word)
            if self.uncovered_word != self.random_word:
                let = input('Input a letter:')
                self.typed_letters.append(let)
                if len(let) > 1 or len(let) == 0:
                    print('You should print a single letter')
                elif self.typed_letters.count(let) > 1:
                    print('You already typed this letter')
                elif let not in string.ascii_lowercase:
                    print('It is not an ASCII lowercase letter')
                elif let in self.random_word:
                    self.uncovered_word = self.uncover_letters(let)
                else:
                    print('No such letter in the word')
                    self.tries_left -= 1
            else:
                print('You guessed the word!\nYou survived!')
                break
        if self.uncovered_word != self.random_word:
            print('You are hanged!')
game = Hangman()
game.start_game()
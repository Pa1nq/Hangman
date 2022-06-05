import random

import time


class Viselica:
    ended = False
    trying = False

    def __init__(self):
        self.mistakes = None
        while not self.mistakes:
            self.mst = input(
                'Hi! Thank you for joining the game "Viselica". Please, enter the difficulty of game: '
                'easy/medium/hard: ')
            if self.mst == 'easy':
                self.mistakes = 10
            elif self.mst == 'medium':
                self.mistakes = 5
            elif self.mst == 'hard':
                self.mistakes = 3
            else:
                print('Not correct name of difficulty, try again')
        self.array = []
        self.word = None
        self.guessed_word = None
        self.sort = []

        lines = open('C://Program Files//Testing//WordsStockRu.txt', 'r', encoding='utf-8')
        read_line = lines.readlines()
        for i in read_line:
            self.array.append(i)

        self.first = input('Game has started! Generate the word with command v.generate()\n')
        while not Viselica.trying:
            if self.first == 'v.generate()':
                Viselica.trying = True
                self.generate()
            else:
                self.first = input('Unknown command! Please, enter v.generate() to generate the word!\n')

    def generate(self):
        self.word = random.choice(self.array)
        self.guessed_word = (len(self.word)-1) * '-'
        after_generate = input(
            'Word has been generated! You can use these commands:\nv.enter_answer to enter the letter '
            'to guess the '
            'word\nv.attempts_left to see how many mistakes do you have\nv.sorted to see the sorted variant of '
            'guessed letters\nv.guessed_word for showing guessed word\n')

        while not Viselica.ended:

            if after_generate == "v.enter_answer":
                order1 = int(input('Please, write an order of letter that you want to enter: '))
                letter1 = input('Cool. Now, please write a letter that you sure is correct: ')
                self.enter_answer(letter=letter1, order=order1)
            elif after_generate == 'v.attempts_left':
                self.attempts_left()
            elif after_generate == 'v.sorted':
                self.sorted_word()
            elif after_generate == 'v.guessed_word':
                self.guessed_worde()
            elif after_generate == 'show_word':
                self.show_word()
            else:
                print('Not a correct command! Try again')
            after_generate = input(
                'You can use these commands:\nv.enter_answer to enter the letter '
                'to guess the '
                'word\nv.attempts_left to see how many attempts do you have\nv.sorted to see the sorted variant of '
                'guessed letters\nv.guessed_word for showing guessed word\n')

    def attempts_left(self):
        print(self.mistakes)

    def enter_answer(self, letter: str, order: int):
        if list(self.word)[order] == letter:
            self.sort.append(letter)
            timen_lst = list(self.guessed_word)
            timen_lst[order] = letter
            self.guessed_word = ''.join([str(elem) for elem in timen_lst])
            print('That was a correct letter! Go on by your luck :D')

            if '-' in self.guessed_word:
                self.guessed_word = self.guessed_word
            else:

                print('You won the game, congratulations! :)')
                Viselica.ended = True
                raise StopIteration('Game ended, you won, congrats!. Thank you for taking part!')

        else:
            self.mistakes -= 1
            self.sort.append(letter)
            if self.mistakes >= 0:
                print(f'There is a mistake! You have {self.mistakes} attempts left, try again')
            else:
                print(f'There is a mistake! You had reached max attempts, and lost.\nGood luck in another game!')
                time.sleep(1.5)
                Viselica.ended = True
                raise StopIteration('Game ended, you lost. Thank you for taking part, and good luck in next tries!')

    def sorted_word(self):
        print(self.sort)

    def show_word(self):
        print(self.word)

    def guessed_worde(self):
        print(sorted(self.guessed_word))


if __name__ == '__main__':
    v = Viselica()

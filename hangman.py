import random

class HangmanPrinter:

    @staticmethod
    def print_hangman(attempts_left, max_attempts):
        if attempts_left == max_attempts:
            print("   |--------")
            print("   |        |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("   |")
            print("   /\\")
            print("  /  \\")
        elif attempts_left == max_attempts - 1:
            print("   |--------")
            print("   |        |")
            print("   |      _---_")
            print("   |     | * * |")
            print("   |      -___-")
            print("   |")
            print("   |")
            print("   /\\")
            print("  /  \\")
        elif attempts_left == max_attempts - 2:
            print("   |--------")
            print("   |        |")
            print("   |      _---_")
            print("   |     | * * |")
            print("   |      -___-")
            print("   |       \\|/")
            print("   |")
            print("   /\\")
            print("  /  \\")
        elif attempts_left == max_attempts - 3:
            print("   |--------")
            print("   |        |")
            print("   |      _---_")
            print("   |     | * * |")
            print("   |      -___-")
            print("   |       \\|/")
            print("   |        |")
            print("   /\\")
            print("  /  \\")
        elif attempts_left == max_attempts - 4:
            print("   |--------")
            print("   |        |")
            print("   |      _---_")
            print("   |     | * * |")
            print("   |      -___-")
            print("   |       \\|/")
            print("   |        |")
            print("   /\\      /")
            print("  /  \\")
        elif attempts_left <= max_attempts - 5:
            print("   |--------")
            print("   |        |")
            print("   |      _---_")
            print("   |     | * * |")
            print("   |      -___-")
            print("   |       \\|/")
            print("   |        |")
            print("   /\\      / \\")
            print("  /  \\")

class Hangman:

    def __init__(self, wordlist, word_to_guess, max_attempts, letters_guessed):
        self.wordlist = wordlist
        self.word_to_guess = word_to_guess
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts
        self.letters_guessed = letters_guessed

    def get_random_word(self):
        with open(self.wordlist, 'r') as file:
            words = file.readlines()

        self.word_to_guess = random.choice(words).strip().lower()
        #print(self.word_to_guess)

    def print_word(self):
        for letter in self.word_to_guess:
            if letter in self.letters_guessed:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

    def guess_letter(self):
        if self.attempts_left <= 0:
            print("Sorry, you've reached the maximum number of attempts. The correct word was:", self.word_to_guess)
            return

        letter = input(f'Guess a letter ({self.attempts_left} attempts left): ')

        if len(letter) != 1:
            print('You can only guess one letter at a time')

        elif not letter.isalpha():
            print('You can only guess letters')

        elif letter in self.letters_guessed:
            print('You already guessed that letter')

        else:
            self.letters_guessed.append(letter)
            if letter not in self.word_to_guess:
                self.attempts_left -= 1

        self.print_word()
        HangmanPrinter.print_hangman(self.attempts_left, self.max_attempts)

        if all(letter in self.letters_guessed for letter in self.word_to_guess):
            print("Congratulations! You've guessed the word:", self.word_to_guess)
        else:
            self.guess_letter()

def main():
    wordlist = 'wordlist.txt'
    letters_guessed = []
    word_to_guess = None
    max_attempts = 5  # Set your desired maximum number of attempts
    game = Hangman(wordlist, word_to_guess, max_attempts, letters_guessed)
    game.get_random_word()
    game.print_word()
    game.guess_letter()

if __name__ == "__main__":
    main()


LIVES = 11

'''
    Hangman model class defines the game behavior.
    It is initialized with a word in which each character must belong to a given dictionary.
    Keeps track of the error_count and remaining_letters_count to determine if the user has won or lost.
    @author Pedro Luis Rivera Gomez
    @date April 13, 2019
'''

class Hangman:

    def __init__(self, word, alphabet):
        self.dictionary = {}
        self.word = word
        self.error_count = 0
        self.init_dictionary(alphabet)
        self.remaining_letters_count = len(self.dictionary.keys())
        self.previous_plays = []

    def init_dictionary(self, alphabet):
        if len(self.word) > 20:
            raise Exception("Input length must be less or equal to 20 characters.")
        for i in range(0, len(self.word)):
            if self.word[i] == ' ':
                continue
            elif self.word[i] not in alphabet:
                raise Exception(self.word[i], " not in alphabet.")
            elif self.word[i] not in self.dictionary.keys():
                self.dictionary[self.word[i]] = [i]
            else:
                self.dictionary[self.word[i]].append(i)

    def play(self, letter):
        if self.has_won() or self.has_lost():
            return "Oops! The game is over!"
        elif letter in self.previous_plays:
            return "You have already selected " + letter + "."
        elif letter in self.dictionary.keys():
            self.previous_plays.append(letter)
            self.remaining_letters_count -= 1
            return self.dictionary.get(letter)
        else:
            self.previous_plays.append(letter)
            self.error_count += 1
            return "Oops! " + letter + " is not part of the solution."

    # Losing condition.
    def has_lost(self):
        return self.error_count == LIVES

    # Winning condition.
    def has_won(self):
        return self.remaining_letters_count == 0

if __name__ == "__main__":
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    hangman = Hangman("LAGARTIJO", alphabet)


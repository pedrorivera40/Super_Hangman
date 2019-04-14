import GameView as gv
from OxfordRequest import OxfordRequest
from time import sleep
from Hangman import Hangman


if __name__ == "__main__":

    # Initialize the views and word generator.
    game_view = gv.HangmanView(1000, 600)
    word_generator = OxfordRequest()

    # English alphabet.
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # Game loop...
    while True:
        # Initialize Hangman Model with word (new) & alphabet. Must validate all characters are within alphabet.
        while True:
            try:
                word = word_generator.get_random_word()
                word = word.upper()
                hangman = Hangman(word, alphabet)
                break
            except:
                print(word + " is not valid.")

        game_view.update_image(0)

        # Draw buttons to their initial state.
        for i in range(0, len(alphabet)):
            game_view.draw_button(i, gv.BUTTON_ACTIVE, alphabet[i])

        # Draw initial word blanks.
        for i in range(0, len(word)):
            if(word[i] == ' '):
                game_view.draw_character(i, ' ')
            else:
                game_view.draw_character(i, '_')

        # While on current game.
        while not hangman.has_won() and not hangman.has_lost():
            player_input = game_view.button_pressed_scanner()
            if player_input == None: # Nothing happened.
                continue
            elif player_input == -1: # Reload Button Pressed.
                game_view.draw_feedback("Let's start from scratch.")
                sleep(2)
                break
            else: # A character button was pressed.
                letter = alphabet[player_input]
                response = hangman.play(letter)
                game_view.draw_button(player_input, gv.BUTTON_PRESSED, letter)
                if type(response) is not str:
                    for j in range(0, len(response)):
                        game_view.draw_character(response[j], letter)
                    response = letter + " is part of the solution."
                game_view.update_image(hangman.error_count)
                game_view.draw_feedback(response)
        game_view.draw_feedback("Game Over!")
        sleep(3)
        if hangman.has_lost(): game_view.draw_feedback("You loose. :|")
        elif hangman.has_won(): game_view.draw_feedback("You win! :D")
        sleep(5)
        game_view.clear_word()
        game_view.draw_feedback("")

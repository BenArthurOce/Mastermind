from cls_game import *
from cls_turn import *

# Client will continue to loop games until exited by the user
while True:
    MastermindGame = Game()
    MastermindGame.isGameRunning = True
    MastermindGame.player_selects_difficulty()
    MastermindGame.construct_correct_answer()
    MastermindGame.build_guess_dictionary_and_answer_list()

    if MastermindGame.gameInformation['difficulty'] == "Debug":
        print(MastermindGame._correctAnswer)


    while MastermindGame.isGameRunning == True:
        MastermindGame.turnNumber += 1


        # if out of turns
        if MastermindGame.turnNumber > MastermindGame.gameInformation ['num_max_guesses']:
            MastermindGame.isGameRunning = False
            MastermindGame.print_game_grid_to_terminal()
            MastermindGame.display.print_lose_screen()
    
        # if not out of turns
        elif MastermindGame.turnNumber <= MastermindGame.gameInformation['num_max_guesses']:
            

            # print the terminal
            MastermindGame.print_game_grid_to_terminal()
            MastermindGame.print_game_instructions_to_terminal()

            # player makes guess
            player_guess = MastermindGame.player_makes_guess()
            MastermindGame.update_guess_dictionary_with_guesses(player_guess)
            MastermindGame.guess_checked_to_answer(player_guess)

            
            # end the game if the player typed "<"
            if MastermindGame.check_if_player_resigned() == True:
                MastermindGame.isGameRunning = False
                MastermindGame.print_game_grid_to_terminal()
                MastermindGame.display.print_lose_screen()

            # if player hits = number of pegs, then the player won
            if MastermindGame.check_if_player_made_correct_guess() == True:
                MastermindGame.isGameRunning = False
                MastermindGame.print_game_grid_to_terminal()
                MastermindGame.display.print_win_screen()

    player_play_again = input("Play Again? (Y/N): ")
    if player_play_again.upper() == "Y" or player_play_again.upper() == "YES":
        continue
    else:
        quit()

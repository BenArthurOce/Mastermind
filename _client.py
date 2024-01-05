from cls_game import *
from cls_turn import *

# b = 8
# list_every_colour = ['RED', 'BLUE', 'YELLOW', 'GREEN', 'ORANGE', 'PURPLE', 'CYAN', 'WHITE', 'MAROON', 'AQUA', 'INDIGO', 'VIOLET', 'TEAL']

# c = list_every_colour[:b]
# print(c)
# input()
while True:
    MastermindGame = Game()
    MastermindGame.set_game_active_true()
    MastermindGame.player_selects_difficulty()
    MastermindGame.build_guess_dictionary_and_answer_list()

    if MastermindGame.game_info_dict['difficulty'] == "Debug":
        print(MastermindGame.correct_answer_list)

    i = 0 #player turn
    while MastermindGame.is_game_active == True:
        i += 1 #increase player turn number

        # if out of turns
        if i > MastermindGame.game_info_dict['num_max_guesses']:
            MastermindGame.set_game_active_false()
            MastermindGame.print_game_grid_to_terminal()
            MastermindGame.print_win_or_lose_to_terminal(did_player_win=False)
    
        # if not out of turns
        elif i <= MastermindGame.game_info_dict['num_max_guesses']:
            NewTurn = Turn(i)
            MastermindGame.print_game_grid_to_terminal()
            
            # player inputs guess and its stored/checked
            player_guess = NewTurn.player_makes_guess(MastermindGame)
            NewTurn.update_guess_dictionary_with_guesses(MastermindGame, player_guess)
            NewTurn.guess_checked_to_answer(MastermindGame, player_guess)

            # end the game if the player typed "<"
            if MastermindGame.check_if_player_resigned() == True:
                MastermindGame.set_game_active_false()
                MastermindGame.print_game_grid_to_terminal()
                MastermindGame.print_win_or_lose_to_terminal(did_player_win=False)

            # if player hits = number of pegs, then the player won
            if MastermindGame.check_if_player_made_correct_guess() == True:
                MastermindGame.set_game_active_false()
                MastermindGame.print_game_grid_to_terminal()
                MastermindGame.print_win_or_lose_to_terminal(did_player_win=True)

    player_play_again = input("Play Again? (Y/N): ")
    if player_play_again.upper() == "Y" or player_play_again.upper() == "YES":
        continue
    else:
        quit()

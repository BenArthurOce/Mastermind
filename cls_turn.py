from cls_game import *

class Turn():
    def __init__(self, turn_num):
        self.turn_num = turn_num


    def player_makes_guess(self, game:Game) -> list:
        """Player types in colours to terminal to make a guess"""

        # display available colours
        game.print_game_instructions_to_terminal()

        # take user input, seperate based on commas and trim
        while True:
            # obtain user input
            user_input_original = [str(i).upper() for i in input ("Enter a Guess: ").split(",")]
            user_input_cleaned = [j.strip() for j in user_input_original]

            # If Player puts in "<", its to resign. Fill the submitted guess with this symbol.
            if "<" in user_input_cleaned:
                if game.game_info_dict['num_pegs'] == 3:
                    return ["<","<","<"]
                elif game.game_info_dict['num_pegs'] == 4:
                    return ["<","<","<","<"]

            # If there is no "<", then continue to check the input normally
            try:    
                # incorrect amount of commas POSSIBLE TODO: (check if exit or instruciton commands used)
                if len(user_input_cleaned) != game.game_info_dict['num_pegs']:
                    raise ValueError()

                else:
                    player_submitted_guess = []
                    for each_guess in user_input_cleaned:
                    
                        # using first letter of input, determine what colour the user is looking for
                        matched_colour=[word for word in game.game_info_dict['list_available_colours'] if word.upper().startswith(each_guess[0])][0]

                        # if all the letters submitted by user appear in the word, then accept
                        if all(item in matched_colour for item in each_guess[1:]) == True:
                            player_submitted_guess.append(matched_colour)

                        else:
                            raise IndexError()
                        
                    return player_submitted_guess
                        
            except ValueError:
                print("\t Input Error: Ensure you have {0:0.0f} Colours, Seperated by {1:0.0f} commas.".format(game.game_info_dict['num_pegs'], game.game_info_dict['num_pegs']-1))

            except IndexError:
                print("\t Input Error: A Colour or Abbreviation you inputted did not match the colours allowed in game")

   

    def guess_checked_to_answer(self, game:Game, list_guess:list) -> None:
        i = self.turn_num
        pegs = game.game_info_dict['num_pegs']

        #Check that guess/answer "pegs" DIRECTLY match and then replace them with "!"
        guessed01 = ["!!" if list_guess[i]  == game.correct_answer_list[i]  else list_guess[i] for i in range (0, pegs) ]
        answer01 = ["!" if game.correct_answer_list[i]  == list_guess[i]  else game.correct_answer_list[i] for i in range (0, pegs) ]

        #Check that guess/answer "pegs" INDIRECTLY match and then replace them with "?"
        for a in range(pegs):
            for b in range(pegs):
                if guessed01[a] == answer01[b]:
                    guessed01[a] = "??"
                    answer01[b] = "?"
                    continue

        # Once Answers and Responses have been coded, provide the hints:
        num_hits = sum(1 for s in guessed01 if '!!' in s)
        num_misses = sum(1 for s in guessed01 if '??' in s)

        game.guess_history_dictionary[i]['hits'] = num_hits
        game.guess_history_dictionary[i]['misses'] = num_misses


    def update_guess_dictionary_with_guesses(self, game:Game, list_guesses:list) -> None:
        i = self.turn_num
        if len(list_guesses) == 3:
            game.guess_history_dictionary[i]['peg1'] = list_guesses[0]
            game.guess_history_dictionary[i]['peg2'] = list_guesses[1]
            game.guess_history_dictionary[i]['peg3'] = list_guesses[2]
        elif len(list_guesses) == 4:
            game.guess_history_dictionary[i]['peg1'] = list_guesses[0]
            game.guess_history_dictionary[i]['peg2'] = list_guesses[1]
            game.guess_history_dictionary[i]['peg3'] = list_guesses[2]
            game.guess_history_dictionary[i]['peg4'] = list_guesses[3]



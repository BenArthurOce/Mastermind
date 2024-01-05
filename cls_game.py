import random
from cls_customDifficulty import *


class Game():
    def __init__(self):
        self.print_welcome_screen_to_terminal()
        self.list_every_colour = ['RED', 'BLUE', 'YELLOW', 'GREEN', 'ORANGE', 'PURPLE', 'CYAN', 'WHITE', 'MAROON', 'AQUA']
        self.game_info_dict = {'difficulty': '', 'list_available_colours':[], 'num_max_colours':0, 'num_max_guesses':0, 'num_pegs':0, 'isRepeatColours':False}
        self.is_game_active = False
        self.correct_answer_list = []
        self.guess_history_dictionary = {}

    def print_welcome_screen_to_terminal(self) -> None:
        """Displays a welcome screen to the player before selecting a difficulty"""
        print(
        '                                         \n'
        '=========================================\n'
        '===============BENS PYTHON===============\n'
        '=============MASTERMIND GAME=============\n'
        '=========================================\n'
        '                                         \n'
        )

    def set_game_active_true(self):
        """Turns game on"""
        self.is_game_active = True

    def set_game_active_false(self):
        """Turns game off"""
        self.is_game_active = False

    def player_selects_difficulty(self) -> None:
        """Player selects a difficulty number and the game stores game elements based on difficulty chosen"""

        ##
        ## START OF OLD (UNUSED) CODE
        ##
        OLDdifficulty_dictionary = {
             'Newbie'   : {'index':1, 'num_max_colours':5, 'num_max_guesses':10, 'num_pegs':3, 'isRepeatColours':False}
            ,'Easy'     : {'index':2, 'num_max_colours':6, 'num_max_guesses':8, 'num_pegs':3, 'isRepeatColours':False}
            ,'Medium'   : {'index':3, 'num_max_colours':7, 'num_max_guesses':6, 'num_pegs':3, 'isRepeatColours':False}
            ,'Hard'     : {'index':4, 'num_max_colours':8, 'num_max_guesses':10, 'num_pegs':4, 'isRepeatColours':False}
            ,'Tricky'   : {'index':5, 'num_max_colours':10, 'num_max_guesses':8, 'num_pegs':4, 'isRepeatColours':True}
            ,'Intense'  : {'index':6, 'num_max_colours':10, 'num_max_guesses':6, 'num_pegs':4, 'isRepeatColours':True}
            ,'Debug'    : {'index':7, 'num_max_colours':4, 'num_max_guesses':4, 'num_pegs':3, 'isRepeatColours':False}
            ,'Custom'   : {'index':8, 'num_max_colours':'?', 'num_max_guesses':'?', 'num_pegs':'?', 'isRepeatColours':'?'}
        }

        OLDdifficulty_index = {1:'Newbie', 2:'Easy', 3:'Medium', 4:'Hard', 5:'Tricky', 6:'Intense', 7:'Debug', 8:'Custom'}

        OLDdifficulty_table_display = (
            '                                                       \n'
            'Num   │ Setting │ Colours │ Guesses │ Pegs  │ Repeats \n'
            '─────────────────────────────────────────────────────  \n'
            '{:<5} │ Newbie  │  {:<5}  │  {:<5}  │ {:<5} │ {} \n'
            '{:<5} │ Easy    │  {:<5}  │  {:<5}  │ {:<5} │ {} \n'
            '{:<5} │ Medium  │  {:<5}  │  {:<5}  │ {:<5} │ {} \n'
            '{:<5} │ Hard    │  {:<5}  │  {:<5}  │ {:<5} │ {} \n'
            '{:<5} │ Tricky  │  {:<5}  │  {:<5}  │ {:<5} │ {} \n'
            '{:<5} │ Intense │  {:<5}  │  {:<5}  │ {:<5} │ {} \n'
            '{:<5} │ Debug   │  {:<5}  │  {:<5}  │ {:<5} │ {} \n'
            '{:<5} │ Custom  │  {:<5}  │  {:<5}  │ {:<5} │ {} \n'
        ).format(
                 *OLDdifficulty_dictionary['Newbie'].values()
                ,*OLDdifficulty_dictionary['Easy'].values()
                ,*OLDdifficulty_dictionary['Medium'].values()
                ,*OLDdifficulty_dictionary['Hard'].values()
                ,*OLDdifficulty_dictionary['Tricky'].values()
                ,*OLDdifficulty_dictionary['Intense'].values()
                ,*OLDdifficulty_dictionary['Debug'].values()
                ,*OLDdifficulty_dictionary['Custom'].values()
                )
        ##
        ## END OF OLD (UNUSED) CODE
        ##


        difficulty_dictionary = {
             1  : {'difficulty':'Newbie',   'num_max_colours':5,    'num_max_guesses':10,   'num_pegs':3,   'isRepeatColours':False}
            ,2  : {'difficulty':'Easy',     'num_max_colours':6,    'num_max_guesses':8,    'num_pegs':3,   'isRepeatColours':False}
            ,3  : {'difficulty':'Medium',   'num_max_colours':7,    'num_max_guesses':6,    'num_pegs':3,   'isRepeatColours':False}
            ,4  : {'difficulty':'Hard',     'num_max_colours':10,   'num_max_guesses':10,   'num_pegs':4,   'isRepeatColours':False}
            ,5  : {'difficulty':'Tough',    'num_max_colours':7,    'num_max_guesses':8,    'num_pegs':3,   'isRepeatColours':True}
            ,6  : {'difficulty':'Tricky',   'num_max_colours':10,   'num_max_guesses':8,    'num_pegs':4,   'isRepeatColours':True}
            ,7  : {'difficulty':'Insane',   'num_max_colours':10,   'num_max_guesses':6,    'num_pegs':4,   'isRepeatColours':True}
            ,8  : {'difficulty':'Debug',    'num_max_colours':4,    'num_max_guesses':5,    'num_pegs':3,   'isRepeatColours':False}
            ,9  : {'difficulty':'Custom',   'num_max_colours':'?',  'num_max_guesses':'?',  'num_pegs':'?', 'isRepeatColours':'?'}
        }

        difficulty_table_display = (
            '                                                       \n'
            'Num   │ Setting │ Colours │ Guesses │ Pegs  │ Repeats  \n'
            '─────────────────────────────────────────────────────  \n'
            ' 1    │ {:<6s}  │  {:<5}  │  {:<5}  │ {:<5} │ {}       \n'
            ' 2    │ {:<6s}  │  {:<5}  │  {:<5}  │ {:<5} │ {}       \n'
            ' 3    │ {:<6s}  │  {:<5}  │  {:<5}  │ {:<5} │ {}       \n'
            ' 4    │ {:<6s}  │  {:<5}  │  {:<5}  │ {:<5} │ {}       \n'
            ' 5    │ {:<6s}  │  {:<5}  │  {:<5}  │ {:<5} │ {}       \n'
            ' 6    │ {:<6s}  │  {:<5}  │  {:<5}  │ {:<5} │ {}       \n'
            ' 7    │ {:<6s}  │  {:<5}  │  {:<5}  │ {:<5} │ {}       \n'
            ' 8    │ {:<6s}  │  {:<5}  │  {:<5}  │ {:<5} │ {}       \n'
            ' 9    │ {:<6s}  │  {:<5}  │  {:<5}  │ {:<5} │ {}       \n'
        ).format(
                 *difficulty_dictionary[1].values()
                ,*difficulty_dictionary[2].values()
                ,*difficulty_dictionary[3].values()
                ,*difficulty_dictionary[4].values()
                ,*difficulty_dictionary[5].values()
                ,*difficulty_dictionary[6].values()
                ,*difficulty_dictionary[7].values()
                ,*difficulty_dictionary[8].values()
                ,*difficulty_dictionary[9].values()
                )

        # print difficulty settings to terminal
        print(difficulty_table_display)

        # user to select a difficulty number
        while True:
            try:
                user_input_int = int(input("Select difficulty index number: "))
                if user_input_int not in list(difficulty_dictionary.keys()):
                    raise ValueError #this will send it to the print message and back to the input option
                break
            except ValueError:
                print("\tError: You are required to enter one of the following: {}".format(difficulty_dictionary.keys()))


        # if user selected custom difficulty  
        if difficulty_dictionary[user_input_int]['difficulty'] == "Custom":
            custom_difficulty = CustomDifficulty()
            custom_difficulty.player_to_select_game_element_types() 
            self.game_info_dict = custom_difficulty.game_settings_dict

            # take the full list of available colours, extract "n" colours, where "n" is number of colours to be used in game
            self.game_info_dict['list_available_colours'] = list(custom_difficulty.game_settings_dict['list_available_colours'])


        # if user selected any other difficulty
        elif difficulty_dictionary[user_input_int]['difficulty'] != "Custom":
            self.game_info_dict = difficulty_dictionary[user_input_int]

            # take the full list of available colours, extract "n" colours, where "n" is number of colours to be used in game
            n = self.game_info_dict['num_max_colours'] 
            self.game_info_dict['list_available_colours'] = self.list_every_colour[:n]  #Set the colours to be used in game



    def build_guess_dictionary_and_answer_list(self) -> None:
        """Game populates the guess dictionary with empty values and 0s as placeholders for when the player makes guesses"""
        pegs = self.game_info_dict['num_pegs']
        repeats = self.game_info_dict['isRepeatColours']

        match pegs, repeats:
            case 3, False:
                for j in range(1, 16): 
                    self.guess_history_dictionary[j] = {'peg1': '--', 'peg2': '--', 'peg3': '--', 'hits':0, 'misses':0}
                    self.correct_answer_list = random.sample(self.game_info_dict['list_available_colours'], self.game_info_dict['num_pegs'])
                    
            case 3, True:
                for j in range(1, 16): 
                    self.guess_history_dictionary[j] = {'peg1': '--', 'peg2': '--', 'peg3': '--', 'hits':0, 'misses':0}
                    self.correct_answer_list = random.choices(self.game_info_dict['list_available_colours'], k = self.game_info_dict['num_pegs'])
                    input("You shouldn't have reached here. Let Ben know.")

            case 4, False:
                for j in range(1, 16): 
                    self.guess_history_dictionary[j] = {'peg1': '--', 'peg2': '--', 'peg3': '--', 'peg4': '--', 'hits':0, 'misses':0}
                    self.correct_answer_list = random.sample(self.game_info_dict['list_available_colours'], self.game_info_dict['num_pegs'])
                    
            case 4, True:
                for j in range(1, 16): 
                    self.guess_history_dictionary[j] = {'peg1': '--', 'peg2': '--', 'peg3': '--', 'peg4': '--', 'hits':0, 'misses':0}                    
                    self.correct_answer_list = random.choices(self.game_info_dict['list_available_colours'], k = self.game_info_dict['num_pegs'])



    def print_game_instructions_to_terminal(self) -> None:
        """Prints the games colours to the terminal"""
        match self.game_info_dict['isRepeatColours']:
            case True:
                display = (
                    '\tColours in Game: {0} \n'
                    '\tType in {1} colours, seperated by {2} commas. Abbreviations allowed \n'
                    '\tType "<" to resign \n'
                    '\tIn this game, colours have a chance to be repeated'
                ).format(
                     self.game_info_dict['list_available_colours']
                    ,self.game_info_dict['num_pegs']
                    ,self.game_info_dict['num_pegs'] - 1
                )
        
            case False:
                display = (
                    '\tColours in Game: {0} \n'
                    '\tType in {1} colours, seperated by {2} commas. Abbreviations allowed \n'
                    '\tType "<" to resign \n'
                    '\tIn this game, colours will not be repeated'
                ).format(
                     self.game_info_dict['list_available_colours']
                    ,self.game_info_dict['num_pegs']
                    ,self.game_info_dict['num_pegs'] - 1
                )
        print('\n' + display + '\n')
        

    def print_game_grid_to_terminal(self):
        """Prints the game board to the player, including previous guesses and hits/misses"""
        pegs = self.game_info_dict['num_pegs']
        g = self.game_info_dict['num_max_guesses']

        # Create the Game Board with all 15 guesses and answer lines (and answer line) based on amount of pegs in the game.
        # Split the game board into a list (one line per element) and print to terminal
        match pegs:
            case 3:
                    board = (
                    '                                                     \n'
                    '                                                     \n'
                    '    GUESS:    │ PEG1   │ PEG2   │ PEG3   │ HITS/NEARS\n'
                    '─────────────────────────────────────────────────────\n'
                    '  1st Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  2nd Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  3rd Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  4th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  5th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  6th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  7th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  8th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  9th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  10th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  11th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  12th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  13th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  14th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  15th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  Answer:     │ {:<6s} │ {:<6s} │ {:<6s} │           \n'
                    '  Answer:     │ {:<6s} │ {:<6s} │ {:<6s} │           \n'
                    ).format(
                             *self.guess_history_dictionary[1].values()
                            ,*self.guess_history_dictionary[2].values()
                            ,*self.guess_history_dictionary[3].values()
                            ,*self.guess_history_dictionary[4].values()
                            ,*self.guess_history_dictionary[5].values()
                            ,*self.guess_history_dictionary[6].values()
                            ,*self.guess_history_dictionary[7].values()
                            ,*self.guess_history_dictionary[8].values()
                            ,*self.guess_history_dictionary[9].values()
                            ,*self.guess_history_dictionary[10].values()
                            ,*self.guess_history_dictionary[11].values()
                            ,*self.guess_history_dictionary[12].values()
                            ,*self.guess_history_dictionary[13].values()
                            ,*self.guess_history_dictionary[14].values()
                            ,*self.guess_history_dictionary[15].values()
                            ,*self.correct_answer_list
                            ,*["??", "??", "??"]
                    ).splitlines() 

            case 4:
                    board = (
                    '                                                              \n'
                    '                                                              \n'
                    '    GUESS:    │ PEG1   │ PEG2   │ PEG3   │ PEG4   │ HITS/NEARS\n'
                    '──────────────────────────────────────────────────────────────\n'
                    '  1st Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  2nd Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  3rd Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  4th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  5th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  6th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  7th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  8th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  9th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  10th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  11th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  12th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  13th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  14th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  15th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
                    '  Answer:     │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │           \n'
                    '  Answer:     │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │           \n'
                    ).format(
                             *self.guess_history_dictionary[1].values()
                            ,*self.guess_history_dictionary[2].values()
                            ,*self.guess_history_dictionary[3].values()
                            ,*self.guess_history_dictionary[4].values()
                            ,*self.guess_history_dictionary[5].values()
                            ,*self.guess_history_dictionary[6].values()
                            ,*self.guess_history_dictionary[7].values()
                            ,*self.guess_history_dictionary[8].values()
                            ,*self.guess_history_dictionary[9].values()
                            ,*self.guess_history_dictionary[10].values()
                            ,*self.guess_history_dictionary[11].values()
                            ,*self.guess_history_dictionary[12].values()
                            ,*self.guess_history_dictionary[13].values()
                            ,*self.guess_history_dictionary[14].values()
                            ,*self.guess_history_dictionary[15].values()
                            ,*self.correct_answer_list
                            ,*["??", "??", "??", "??"]
                    ).splitlines() 

        # Print each line of the Game Board, up to the number of guesses the player is allowed to have
        for a in range(g+4):
            print(board[a])

        # if game is ongoing, print the Answer: ?? line to the terminal
        if self.is_game_active == True:
            print(board[-1:][0])

        # if game is complete, print the correct answer line to the terminal
        elif self.is_game_active == False:
            print(board[-2:][0])


    def check_if_player_resigned(self) -> bool:
        """Checks player guesses for the "<" symbol. If this was entered, then the player resigned """
        for j in self.guess_history_dictionary:
            if self.guess_history_dictionary[j]['peg1'] == "<":
                return True
        return False
    

    def check_if_player_made_correct_guess(self) -> bool:
        """Checks to see if the player made the correct guess by going through the history of guesses, and finding if 'hits' matches 'num_pegs' """
        pegs = self.game_info_dict['num_pegs']

        for j in self.guess_history_dictionary:
            if self.guess_history_dictionary[j]['hits'] == pegs:
                return True
        return False


    def print_win_or_lose_to_terminal(self, did_player_win:bool) -> None:
        """Inform player if they won or lost"""
        if did_player_win == True:
            print("==========================================")
            print("================YOU WON!==================")
            print("==========================================")
            print()
        if did_player_win == False:
            print("==========================================")
            print("===============TRY AGAIN!=================")
            print("==========================================")
            print()

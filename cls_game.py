import random
from cls_customDifficulty import *
from cls_display import *

DIFFICULTY_DICTIONARY = {
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

POSSIBLE_GEMSTONES = ["AMBER", "BERYL", "CORAL", "DIAMOND", "EMERALD", "GARNET", "JADE", "LAPIS", "MOONSTONE", "OPAL", "PEARL", "QUARTZ", "RUBY", "SAPPHIRE", "TOPAZ", "ZIRCON"]
POSSIBLE_COLOURS = ['AQUA', 'BLUE', 'CYAN', 'GREEN', 'INDIGO', 'LIME', 'MAROON', 'NAVY', 'ORANGE', 'PINK', 'RED', 'TEAL', 'VOILET', 'WHITE', 'YELLOW']


class Game():
    def __init__(self):
        self.display = Display()
        self._turnNumber = 0
        self._gameInformation = {'difficulty': '', 'list_available_gemstones':[], 'num_max_colours':0, 'num_max_guesses':0, 'num_pegs':0, 'isRepeatColours':False}
        self._isGameRunning = False
        self._selectedDifficulty = -1
        self._previousGuessDict = {}
        self._correctAnswer = []

    ##
    ## turnNumber
    ##
    @property
    def turnNumber(self):
        """turnNumber getter"""
        return self._turnNumber
    
    @turnNumber.setter
    def turnNumber(self, value):
        """turnNumber setter"""
        self._turnNumber = value

    ##
    ## gameInformation
    ##
    @property
    def gameInformation(self):
        """gameInformation getter"""
        return self._gameInformation
    
    @gameInformation.setter
    def gameInformation(self, value):
        """gameInformation setter"""
        self._gameInformation = value

    ##
    ## isGameRunning
    ##
    @property
    def isGameRunning(self):
        """isGameRunning getter"""
        return self._isGameRunning

    @isGameRunning.setter
    def isGameRunning(self, value):
        """isGameRunning setter"""
        self._isGameRunning = value

    ##
    ## selectedDifficulty
    ##
    @property
    def selectedDifficulty(self):
        """selectedDifficulty getter"""
        return self._selectedDifficulty

    @selectedDifficulty.setter
    def selectedDifficulty(self, value):
        """selectedDifficulty setter"""
        self._selectedDifficulty = value

    ##
    ## previousGuessDict
    ##
    @property
    def previousGuessDict(self):
        """Getter method"""
        return self._previousGuessDict

    @previousGuessDict.setter
    def previousGuessDict(self, new_info):
        self._previousGuessDict.update(new_info)


    ##
    ## correctAnswer
    ##
    @property
    def correctAnswer(self):
        """Getter method"""
        return self._correctAnswer

    @correctAnswer.setter
    def correctAnswer(self, value):
        self._correctAnswer = value




    def player_selects_difficulty(self) -> int:
        """Player selects a difficulty number and the game stores game elements based on difficulty chosen"""
        self.display.print_welcome_screen_to_terminal()
        self.display.print_difficulty_options_to_terminal()
        self.selectedDifficulty = int(restrict_user_input_numerical(list(DIFFICULTY_DICTIONARY.keys()), "Select Difficulty:"))
        self.gameInformation = DIFFICULTY_DICTIONARY[self.selectedDifficulty]
    

    def construct_correct_answer(self) -> None:
        # self.gameInformation = DIFFICULTY_DICTIONARY[self.selected_difficulty]

        # take the full list of available colours, extract "n" colours, where "n" is number of colours to be used in game
        n = self.gameInformation['num_max_colours'] 
        self.gameInformation['list_available_gemstones'] = POSSIBLE_GEMSTONES[:n]  #Set the colours to be used in game
        # # if user selected custom difficulty  
        # if difficulty_dictionary[user_input_int]['difficulty'] == "Custom":
        #     custom_difficulty = CustomDifficulty()
        #     custom_difficulty.player_to_select_game_element_types() 
        #     self.gameInformation = custom_difficulty.game_settings_dict

        #     # take the full list of available colours, extract "n" colours, where "n" is number of colours to be used in game
        #     self.gameInformation['list_available_gemstones'] = list(custom_difficulty.game_settings_dict['list_available_gemstones'])


        # # if user selected any other difficulty
        # elif difficulty_dictionary[user_input_int]['difficulty'] != "Custom":
        #     self.gameInformation = difficulty_dictionary[user_input_int]

        #     # take the full list of available colours, extract "n" colours, where "n" is number of colours to be used in game
        #     n = self.gameInformation['num_max_colours'] 
        #     self.gameInformation['list_available_gemstones'] = POSSIBLE_GEMSTONES[:n]  #Set the colours to be used in game
        # pass

    def player_makes_guess(self):
        # take user input, seperate based on commas and trim
        while True:
            # obtain user input
            user_input_original = [str(i).upper() for i in input ("Enter a Guess: ").split(",")]
            user_input_cleaned = [j.strip() for j in user_input_original]

            # If Player puts in "<", its to resign. Fill the submitted guess with this symbol.
            if "<" in user_input_cleaned:
                if self.gameInformation['num_pegs'] == 3:
                    return ["<","<","<"]
                elif self.gameInformation['num_pegs'] == 4:
                    return ["<","<","<","<"]

            # If there is no "<", then continue to check the input normally
            try:    
                # incorrect amount of commas POSSIBLE TODO: (check if exit or instruciton commands used)
                if len(user_input_cleaned) != self.gameInformation['num_pegs']:
                    raise ValueError()

                else:
                    player_submitted_guess = []
                    for each_guess in user_input_cleaned:
                    
                        # using first letter of input, determine what colour the user is looking for
                        matched_colour=[word for word in self.gameInformation['list_available_gemstones'] if word.upper().startswith(each_guess[0])][0]

                        # if all the letters submitted by user appear in the word, then accept
                        if all(item in matched_colour for item in each_guess[1:]) == True:
                            player_submitted_guess.append(matched_colour)

                        else:
                            raise IndexError()
                    print(player_submitted_guess)
                    return player_submitted_guess
                        
            except ValueError:
                print("\t Input Error: Ensure you have {0:0.0f} Gems, Seperated by {1:0.0f} commas.".format(self.gameInformation['num_pegs'], self.gameInformation['num_pegs']-1))

            except IndexError:
                print(self.gameInformation)
                print("\t Input Error: A Colour or Abbreviation you inputted did not match the gems allowed in game")

   

    def guess_checked_to_answer(self, list_guess:list) -> None:
        i = self.turnNumber
        pegs = self.gameInformation['num_pegs']

        #Check that guess/answer "pegs" DIRECTLY match and then replace them with "!"
        guessed01 = ["!!" if list_guess[i]  == self.correctAnswer[i]  else list_guess[i] for i in range (0, pegs) ]
        answer01 = ["!" if self.correctAnswer[i]  == list_guess[i]  else self.correctAnswer[i] for i in range (0, pegs) ]

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



        self.previousGuessDict[i]['hits'] = num_hits
        self.previousGuessDict[i]['misses'] = num_misses


    def update_guess_dictionary_with_guesses(self, list_guesses:list) -> None:
        i = self.turnNumber
        if len(list_guesses) == 3:
            self.previousGuessDict[i]['peg1'] = list_guesses[0]
            self.previousGuessDict[i]['peg2'] = list_guesses[1]
            self.previousGuessDict[i]['peg3'] = list_guesses[2]
        elif len(list_guesses) == 4:
            self.previousGuessDict[i]['peg1'] = list_guesses[0]
            self.previousGuessDict[i]['peg2'] = list_guesses[1]
            self.previousGuessDict[i]['peg3'] = list_guesses[2]
            self.previousGuessDict[i]['peg4'] = list_guesses[3]



    def print_game_grid_to_terminal(self) -> None:
        self.display.print_game_grid_to_terminal(
            self.gameInformation['num_pegs']
            ,self.gameInformation['num_max_guesses']
            ,self.previousGuessDict
            ,self._correctAnswer
            ,self.isGameRunning
        )



    def player_selects_difficulty2(self) -> None:
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




        # user to select a difficulty number
        while True:
            try:
                user_input_int = int(input("Select difficulty index number: "))
                if user_input_int not in list(DIFFICULTY_DICTIONARY.keys()):
                    raise ValueError #this will send it to the print message and back to the input option
                break
            except ValueError:
                print("\tError: You are required to enter one of the following: {}".format(DIFFICULTY_DICTIONARY.keys()))






    def build_guess_dictionary_and_answer_list(self) -> None:
        """Game populates the guess dictionary with empty values and 0s as placeholders for when the player makes guesses"""
        pegs = self.gameInformation['num_pegs']
        repeats = self.gameInformation['isRepeatColours']

        match pegs, repeats:
            case 3, False:
                for j in range(1, 16): 
                    self.previousGuessDict[j] = {'peg1': '--', 'peg2': '--', 'peg3': '--', 'hits':0, 'misses':0}
                    self._correctAnswer = random.sample(self.gameInformation['list_available_gemstones'], self.gameInformation['num_pegs'])
                    
            case 3, True:
                for j in range(1, 16): 
                    self.previousGuessDict[j] = {'peg1': '--', 'peg2': '--', 'peg3': '--', 'hits':0, 'misses':0}
                    self._correctAnswer = random.choices(self.gameInformation['list_available_gemstones'], k = self.gameInformation['num_pegs'])
                    input("You shouldn't have reached here. Let Ben know.")

            case 4, False:
                for j in range(1, 16): 
                    self.previousGuessDict[j] = {'peg1': '--', 'peg2': '--', 'peg3': '--', 'peg4': '--', 'hits':0, 'misses':0}
                    self._correctAnswer = random.sample(self.gameInformation['list_available_gemstones'], self.gameInformation['num_pegs'])
                    
            case 4, True:
                for j in range(1, 16): 
                    self.previousGuessDict[j] = {'peg1': '--', 'peg2': '--', 'peg3': '--', 'peg4': '--', 'hits':0, 'misses':0}                    
                    self._correctAnswer = random.choices(self.gameInformation['list_available_gemstones'], k = self.gameInformation['num_pegs'])



    def print_game_instructions_to_terminal(self) -> None:
        """Prints the games colours to the terminal"""
        match self.gameInformation['isRepeatColours']:
            case True:
                display = (
                    '\tColours in Game: {0} \n'
                    '\tType in {1} colours, seperated by {2} commas. Abbreviations allowed \n'
                    '\tType "<" to resign \n'
                    '\tIn this game, colours have a chance to be repeated'
                ).format(
                     self.gameInformation['list_available_gemstones']
                    ,self.gameInformation['num_pegs']
                    ,self.gameInformation['num_pegs'] - 1
                )
        
            case False:
                display = (
                    '\tColours in Game: {0} \n'
                    '\tType in {1} colours, seperated by {2} commas. Abbreviations allowed \n'
                    '\tType "<" to resign \n'
                    '\tIn this game, colours will not be repeated'
                ).format(
                     self.gameInformation['list_available_gemstones']
                    ,self.gameInformation['num_pegs']
                    ,self.gameInformation['num_pegs'] - 1
                )
        print('\n' + display + '\n')
        

    # def print_game_grid_to_terminal(self):
    #     """Prints the game board to the player, including previous guesses and hits/misses"""
    #     pegs = self.gameInformation['num_pegs']
    #     g = self.gameInformation['num_max_guesses']

    #     # Create the Game Board with all 15 guesses and answer lines (and answer line) based on amount of pegs in the game.
    #     # Split the game board into a list (one line per element) and print to terminal
    #     match pegs:
    #         case 3:
    #                 board = (
    #                 '                                                     \n'
    #                 '                                                     \n'
    #                 '    GUESS:    │ PEG1   │ PEG2   │ PEG3   │ HITS/NEARS\n'
    #                 '─────────────────────────────────────────────────────\n'
    #                 '  1st Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  2nd Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  3rd Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  4th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  5th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  6th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  7th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  8th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  9th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  10th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  11th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  12th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  13th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  14th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  15th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  Answer:     │ {:<6s} │ {:<6s} │ {:<6s} │           \n'
    #                 '  Answer:     │ {:<6s} │ {:<6s} │ {:<6s} │           \n'
    #                 ).format(
    #                          *self.previousGuessDict[1].values()
    #                         ,*self.previousGuessDict[2].values()
    #                         ,*self.previousGuessDict[3].values()
    #                         ,*self.previousGuessDict[4].values()
    #                         ,*self.previousGuessDict[5].values()
    #                         ,*self.previousGuessDict[6].values()
    #                         ,*self.previousGuessDict[7].values()
    #                         ,*self.previousGuessDict[8].values()
    #                         ,*self.previousGuessDict[9].values()
    #                         ,*self.previousGuessDict[10].values()
    #                         ,*self.previousGuessDict[11].values()
    #                         ,*self.previousGuessDict[12].values()
    #                         ,*self.previousGuessDict[13].values()
    #                         ,*self.previousGuessDict[14].values()
    #                         ,*self.previousGuessDict[15].values()
    #                         ,*self._correctAnswer
    #                         ,*["??", "??", "??"]
    #                 ).splitlines()

    #         case 4:
    #                 board = (
    #                 '                                                              \n'
    #                 '                                                              \n'
    #                 '    GUESS:    │ PEG1   │ PEG2   │ PEG3   │ PEG4   │ HITS/NEARS\n'
    #                 '──────────────────────────────────────────────────────────────\n'
    #                 '  1st Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  2nd Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  3rd Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  4th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  5th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  6th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  7th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  8th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  9th Guess:  │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  10th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  11th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  12th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  13th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  14th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  15th Guess: │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │  {}/{}    \n'
    #                 '  Answer:     │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │           \n'
    #                 '  Answer:     │ {:<6s} │ {:<6s} │ {:<6s} │ {:<6s} │           \n'
    #                 ).format(
    #                          *self.previousGuessDict[1].values()
    #                         ,*self.previousGuessDict[2].values()
    #                         ,*self.previousGuessDict[3].values()
    #                         ,*self.previousGuessDict[4].values()
    #                         ,*self.previousGuessDict[5].values()
    #                         ,*self.previousGuessDict[6].values()
    #                         ,*self.previousGuessDict[7].values()
    #                         ,*self.previousGuessDict[8].values()
    #                         ,*self.previousGuessDict[9].values()
    #                         ,*self.previousGuessDict[10].values()
    #                         ,*self.previousGuessDict[11].values()
    #                         ,*self.previousGuessDict[12].values()
    #                         ,*self.previousGuessDict[13].values()
    #                         ,*self.previousGuessDict[14].values()
    #                         ,*self.previousGuessDict[15].values()
    #                         ,*self._correctAnswer
    #                         ,*["??", "??", "??", "??"]
    #                 ).splitlines() 

    #     # Print each line of the Game Board, up to the number of guesses the player is allowed to have
    #     for a in range(g+4):
    #         print(board[a])

    #     # if game is ongoing, print the Answer: ?? line to the terminal
    #     if self.isGameRunning == True:
    #         print(board[-1:][0])

    #     # if game is complete, print the correct answer line to the terminal
    #     elif self.isGameRunning == False:
    #         print(board[-2:][0])


    def check_if_player_resigned(self) -> bool:
        """Checks player guesses for the "<" symbol. If this was entered, then the player resigned """
        for j in self.previousGuessDict:
            if self.previousGuessDict[j]['peg1'] == "<":
                return True
        return False
    

    def check_if_player_made_correct_guess(self) -> bool:
        """Checks to see if the player made the correct guess by going through the history of guesses, and finding if 'hits' matches 'num_pegs' """
        pegs = self.gameInformation['num_pegs']

        for j in self.previousGuessDict:
            if self.previousGuessDict[j]['hits'] == pegs:
                return True
        return False


    # def print_win_or_lose_to_terminal(self, did_player_win:bool) -> None:
    #     """Inform player if they won or lost"""
    #     if did_player_win == True:
    #         print("==========================================")
    #         print("================YOU WON!==================")
    #         print("==========================================")
    #         print()
    #     if did_player_win == False:
    #         print("==========================================")
    #         print("===============TRY AGAIN!=================")
    #         print("==========================================")
    #         print()



def restrict_user_input_numerical(user_can_only_type:list, input_message:str):
    while True:
        try:
            user_input = input(input_message + ": ")
            if int(user_input) in user_can_only_type:
                return user_input
            raise ValueError()
        except ValueError:
            print("    Error: You are required to enter one of the following: {}".format(user_can_only_type))
            print("    Please try again\n")
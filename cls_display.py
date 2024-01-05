class Display():
    def __init__(self):
        pass


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

    def print_win_screen(self) -> None:
        print(
        '=========================================\n'
        '=================YOU WON!================\n'
        '=========================================\n'
        )

    def print_lose_screen(self) -> None:
        print(
        '=========================================\n'
        '================TRY AGAIN!===============\n'
        '=========================================\n'
        )

    def print_game_grid_to_terminal(self, num_pegs, max_guesses, previousGuessDict:dict, _correctAnswer:list, isGameRunning:bool):
        """Prints the game board to the player, including previous guesses and hits/misses"""

        # Create the Game Board with all 15 guesses and answer lines (and answer line) based on amount of pegs in the game.
        # Split the game board into a list (one line per element) and print to terminal
        match num_pegs:
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
                             *previousGuessDict[1].values()
                            ,*previousGuessDict[2].values()
                            ,*previousGuessDict[3].values()
                            ,*previousGuessDict[4].values()
                            ,*previousGuessDict[5].values()
                            ,*previousGuessDict[6].values()
                            ,*previousGuessDict[7].values()
                            ,*previousGuessDict[8].values()
                            ,*previousGuessDict[9].values()
                            ,*previousGuessDict[10].values()
                            ,*previousGuessDict[11].values()
                            ,*previousGuessDict[12].values()
                            ,*previousGuessDict[13].values()
                            ,*previousGuessDict[14].values()
                            ,*previousGuessDict[15].values()
                            ,*_correctAnswer
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
                             *previousGuessDict[1].values()
                            ,*previousGuessDict[2].values()
                            ,*previousGuessDict[3].values()
                            ,*previousGuessDict[4].values()
                            ,*previousGuessDict[5].values()
                            ,*previousGuessDict[6].values()
                            ,*previousGuessDict[7].values()
                            ,*previousGuessDict[8].values()
                            ,*previousGuessDict[9].values()
                            ,*previousGuessDict[10].values()
                            ,*previousGuessDict[11].values()
                            ,*previousGuessDict[12].values()
                            ,*previousGuessDict[13].values()
                            ,*previousGuessDict[14].values()
                            ,*previousGuessDict[15].values()
                            ,*_correctAnswer
                            ,*["??", "??", "??", "??"]
                    ).splitlines() 

        # Print each line of the Game Board, up to the number of guesses the player is allowed to have
        for a in range(max_guesses+4):
            print(board[a])

        # if game is ongoing, print the Answer: ?? line to the terminal
        if isGameRunning == True:
            print(board[-1:][0])

        # if game is complete, print the correct answer line to the terminal
        elif isGameRunning == False:
            print(board[-2:][0])


    def print_game_instructions_to_terminal(self, game_info_dict:dict) -> None:
        """Prints the games colours to the terminal"""
        match game_info_dict['isRepeatColours']:
            case True:
                display = (
                    '\tColours in Game: {0} \n'
                    '\tType in {1} colours, seperated by {2} commas. Abbreviations allowed \n'
                    '\tType "<" to resign \n'
                    '\tIn this game, colours have a chance to be repeated'
                ).format(
                     game_info_dict['list_available_gemstones']
                    ,game_info_dict['num_pegs']
                    ,game_info_dict['num_pegs'] - 1
                )
        
            case False:
                display = (
                    '\tColours in Game: {0} \n'
                    '\tType in {1} colours, seperated by {2} commas. Abbreviations allowed \n'
                    '\tType "<" to resign \n'
                    '\tIn this game, colours will not be repeated'
                ).format(
                     game_info_dict['list_available_gemstones']
                    ,game_info_dict['num_pegs']
                    ,game_info_dict['num_pegs'] - 1
                )
        print('\n' + display + '\n')



    def print_difficulty_options_to_terminal(self):
        difficulty_dictionary = {
             1  : {'difficulty':'Newbie',   'num_max_gemstone':5,    'num_max_guesses':10,   'num_pegs':3,   'isRepeatColours':False}
            ,2  : {'difficulty':'Easy',     'num_max_gemstone':6,    'num_max_guesses':8,    'num_pegs':3,   'isRepeatColours':False}
            ,3  : {'difficulty':'Medium',   'num_max_gemstone':7,    'num_max_guesses':6,    'num_pegs':3,   'isRepeatColours':False}
            ,4  : {'difficulty':'Hard',     'num_max_gemstone':10,   'num_max_guesses':10,   'num_pegs':4,   'isRepeatColours':False}
            ,5  : {'difficulty':'Tough',    'num_max_gemstone':7,    'num_max_guesses':8,    'num_pegs':3,   'isRepeatColours':True}
            ,6  : {'difficulty':'Tricky',   'num_max_gemstone':10,   'num_max_guesses':8,    'num_pegs':4,   'isRepeatColours':True}
            ,7  : {'difficulty':'Insane',   'num_max_gemstone':10,   'num_max_guesses':6,    'num_pegs':4,   'isRepeatColours':True}
            ,8  : {'difficulty':'Debug',    'num_max_gemstone':4,    'num_max_guesses':5,    'num_pegs':3,   'isRepeatColours':False}
            ,9  : {'difficulty':'Custom',   'num_max_gemstone':'?',  'num_max_guesses':'?',  'num_pegs':'?', 'isRepeatColours':'?'}
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
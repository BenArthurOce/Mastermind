from random import randrange
import random



#GLOBAL LIST FOR COLOURS USED
#=============================
rRed =      ['RED',     'RED',  'RD', 'RE']
rBlue    =  ['BLUE',    'BLU',  'BL', 'BL']
rYellow =   ['YELLOW',  'YLO',  'YL', 'YE', 'YW']
rGreen =    ['GREEN',   'GRN',  'GR', 'GN']
rOrange =   ['ORANGE',  'ORG',  'OR', 'OG']
rPurple =   ['PURPLE',  'PPL',  'PL', 'PR']
rCyan =     ['CYAN',    'CYN',  'CY', 'CN']
rBrown =    ['BROWN',   'BRN',  'BR', 'BN']
rWhite =    ['WHITE',   'WHT',  'WT', 'WH']
rPink =     ['PINK',    'PNK',  'PK', 'PN']
rFull_Colour_List = [rRed,rBlue,rYellow,rGreen,rOrange,rPurple,rCyan,rBrown,rWhite,rPink]

rAll_Input_Options = [j for i in rFull_Colour_List for j in i]  # every input option
rAllColours_FullNames = [a[0] for a in rFull_Colour_List]            # every full name of all 10 colours
rAllColours_3CharNames = [a[1] for a in rFull_Colour_List]           # every 3character shortcut of all 10 colours
rAllColours_2CharNames = [x for x in rAll_Input_Options if x not in rAllColours_FullNames and x not in rAllColours_3CharNames]

#GAME COLOURS - COLOURS AVAILABLE BY PLAYER TO INPUT
#============================
rGameInput_AllOptions = []
rGameColours_FullNames = []
rGameColours_3CharNames = []
rGameColours_2CharNames = []

#GAME CORRECT ANSWER
#============================
rCorrectAnswer = []

#GAME DIFFICULTY - SET BY PLAYER IN FUNCTION INPUT
#============================
iColoursThatPlayerCanUse = 0
iTurnsAllowed = 0
iBoardSize = 0
blnMaxOneOfEachColour = False

#Debugging Test
# rDummyInput = ["RED","GREEN","BLUE","YELLOW"]
# rDummyInput = ["RD","GR","YL","ORG"]

#PLAYER INPUT HISTORY
#============================
rPlayerResponses = []
rPlayerHitsNears = []

#===========================================
#========DISPLAY FUNCTIONS==================
#===========================================
def fConstructGameBoard(board_size):

    # shorten the code for print lines
    resp  = [a for a in rPlayerResponses]
    shots = [a for a in rPlayerHitsNears]
    ans   = [a for a in rCorrectAnswer] 

    #-----------------
    #---3 PEG BOARD---
    #-----------------
    if board_size == 3:
            return (

                '    GUESS:   │  PEG1  │  PEG2  │  PEG3  │ HITS/NEARS\n'
                '────────────────────────────────────────────────────\n'
                '  1st Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  2nd Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  3rd Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  4th Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  5th Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  6th Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  7th Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  8th Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  9th Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                ' 10th Guess: │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '     Answer: │ {:000} │ {:000} │ {:000} │           \n'
                '     Answer: │   ??   │   ??   │   ??   │           \n'

            ).format(
                #   PEG ONE                     PEG TWO                   PEG THREE                                                HITS                   MISSES                
                format(resp[0][0], ' <6'), format(resp[0][1], ' <6'), format(resp[0][2], ' <6'),                            format(shots[0][0]),    format(shots[0][1]),            #Guess 1
                format(resp[1][0], ' <6'), format(resp[1][1], ' <6'), format(resp[1][2], ' <6'),                            format(shots[1][0]),    format(shots[1][1]),            #Guess 2
                format(resp[2][0], ' <6'), format(resp[2][1], ' <6'), format(resp[2][2], ' <6'),                            format(shots[2][0]),    format(shots[2][1]),            #Guess 3
                format(resp[3][0], ' <6'), format(resp[3][1], ' <6'), format(resp[3][2], ' <6'),                            format(shots[3][0]),    format(shots[3][1]),            #Guess 4
                format(resp[4][0], ' <6'), format(resp[4][1], ' <6'), format(resp[4][2], ' <6'),                            format(shots[4][0]),    format(shots[4][1]),            #Guess 5
                format(resp[5][0], ' <6'), format(resp[5][1], ' <6'), format(resp[5][2], ' <6'),                            format(shots[5][0]),    format(shots[5][1]),            #Guess 6
                format(resp[6][0], ' <6'), format(resp[6][1], ' <6'), format(resp[6][2], ' <6'),                            format(shots[6][0]),    format(shots[6][1]),            #Guess 7
                format(resp[7][0], ' <6'), format(resp[7][1], ' <6'), format(resp[7][2], ' <6'),                            format(shots[7][0]),    format(shots[7][1]),            #Guess 8
                format(resp[8][0], ' <6'), format(resp[8][1], ' <6'), format(resp[8][2], ' <6'),                            format(shots[8][0]),    format(shots[8][1]),            #Guess 9
                format(resp[9][0], ' <6'), format(resp[9][1], ' <6'), format(resp[9][2], ' <6'),                            format(shots[9][0]),    format(shots[9][1]),            #Guess 10
                format(ans[0]    , ' <6'), format(ans[1]    , ' <6'), format(ans[2]    , ' <6')                                                                                     #Answer
            ).splitlines() 

    #-----------------
    #---4 PEG BOARD---
    #-----------------
    if board_size == 4:
            return (

                '    GUESS:   │  PEG1  │  PEG2  │  PEG3  │  PEG4  │ HITS/NEARS\n'
                '─────────────────────────────────────────────────────────────\n'
                '  1st Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  2nd Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  3rd Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  4th Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  5th Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  6th Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  7th Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  8th Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '  9th Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                ' 10th Guess: │ {:000} │ {:000} │ {:000} │ {:000} │ {}/{}     \n'
                '     Answer: │ {:000} │ {:000} │ {:000} │ {:000} │           \n'
                '     Answer: │   ??   │   ??   │   ??   │   ??   │           \n'

            ).format(
                #   PEG ONE                     PEG TWO                   PEG THREE                   PEG FOUR                        HITS                   MISSES                
                format(resp[0][0], ' <6'), format(resp[0][1], ' <6'), format(resp[0][2], ' <6'), format(resp[0][3], ' <6'),    format(shots[0][0]),    format(shots[0][1]),            #Guess 1
                format(resp[1][0], ' <6'), format(resp[1][1], ' <6'), format(resp[1][2], ' <6'), format(resp[1][3], ' <6'),    format(shots[1][0]),    format(shots[1][1]),            #Guess 2
                format(resp[2][0], ' <6'), format(resp[2][1], ' <6'), format(resp[2][2], ' <6'), format(resp[2][3], ' <6'),    format(shots[2][0]),    format(shots[2][1]),            #Guess 3
                format(resp[3][0], ' <6'), format(resp[3][1], ' <6'), format(resp[3][2], ' <6'), format(resp[3][3], ' <6'),    format(shots[3][0]),    format(shots[3][1]),            #Guess 4
                format(resp[4][0], ' <6'), format(resp[4][1], ' <6'), format(resp[4][2], ' <6'), format(resp[4][3], ' <6'),    format(shots[4][0]),    format(shots[4][1]),            #Guess 5
                format(resp[5][0], ' <6'), format(resp[5][1], ' <6'), format(resp[5][2], ' <6'), format(resp[5][3], ' <6'),    format(shots[5][0]),    format(shots[5][1]),            #Guess 6
                format(resp[6][0], ' <6'), format(resp[6][1], ' <6'), format(resp[6][2], ' <6'), format(resp[6][3], ' <6'),    format(shots[6][0]),    format(shots[6][1]),            #Guess 7
                format(resp[7][0], ' <6'), format(resp[7][1], ' <6'), format(resp[7][2], ' <6'), format(resp[7][3], ' <6'),    format(shots[7][0]),    format(shots[7][1]),            #Guess 8
                format(resp[8][0], ' <6'), format(resp[8][1], ' <6'), format(resp[8][2], ' <6'), format(resp[8][3], ' <6'),    format(shots[8][0]),    format(shots[8][1]),            #Guess 9
                format(resp[9][0], ' <6'), format(resp[9][1], ' <6'), format(resp[9][2], ' <6'), format(resp[9][3], ' <6'),    format(shots[9][0]),    format(shots[9][1]),            #Guess 10
                format(ans[0]    , ' <6'), format(ans[1]    , ' <6'), format(ans[2]    , ' <6'), format(ans[3]    , ' <6')                                                             #Answer
            ).splitlines()  


def fDisplayBoard(bln_reveal_answer):
    # generate board header, guesses and answer into a list
    board_lines = fConstructGameBoard(iBoardSize)

    # calculate number of lines to be printed
    num_lines = iTurnsAllowed + 2       # +2 being the header line and seperator

    #print each line to terminal
    print('\n')
    for a in range(num_lines):
        print(board_lines[a])

    #print the "??" answer or the actual answer
    if bln_reveal_answer == False:
        print(board_lines[13]+'\n')
    elif bln_reveal_answer == True:
        print(board_lines[12]+'\n')


def fDisplay_Input_Options():
#---[COLLECT INPUT OPTIONS]
    #Prints a Grid in the terminal that lists each colour available in the game, and their shortcuts that can be keyed in
    rList01_All_Char = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    rList02_Three_Char = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    rList03_Two_Char = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    header = ["Full Colour: ","3 Chars: ","2 Chars: "]

    # #Combine the three lists into a single list that holds all
    rGrid = [rList01_All_Char, rList02_Three_Char, rList03_Two_Char]

    # #Check Index[0] of list. If its not a colour used this game, replace it with "-"
    for y in range(len(rGameColours_FullNames)):
        investigate_col = rAllColours_FullNames[y]
        if investigate_col in rGameColours_FullNames:
            rList01_All_Char[y] = rGameColours_FullNames[y]
            rList02_Three_Char[y] = rGameColours_3CharNames[y]
            rList03_Two_Char[y] = rGameColours_2CharNames[y]
            

#---[DISPLAY INPUT OPTIONS]
    print("  Enter your Colours: ({0} colours, seperated with a comma)".format(iBoardSize))
    print("─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

    j = -1
    for i in rGrid:
        j += 1
        print("{0:15} │ {1:7} │ {2:7} │ {3:7} │ {4:7} │ {5:7} │ {6:7} │ {7:7} │ {8:7} │ {9:7} │ {10:7} │ ".format(header[j].rjust(15),i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
    return


def fDisplay_Win_Or_Lose(did_player_win):
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

    input("Thank you for playing, press any key to exit program")
    quit()
    

#===========================================
#========USER INPUT, ERROR CHECK============
#===========================================

def fPlayerInput0_Nexus():

    non_guess_list =["<","Resign","Display"]

    while True:
        fDisplay_Input_Options()    # display grid of game board and colours to choose

        # player inputs a string. Error checking for input done here
        rTyped_input_line = fUser_Inputs_Colours(non_guess_list)

        # check for non guess options like resigning
        if "<" in rTyped_input_line or "Resign" in rTyped_input_line or "Display" in rTyped_input_line:
            rTyped_input_line = rTyped_input_line.upper()
            if "<" in rTyped_input_line:
                input("test hello. This code will go to instructions")
            if "Resign".upper() in rTyped_input_line:
                fDisplayBoard(bln_reveal_answer=True)
                fDisplay_Win_Or_Lose(did_player_win=False)
            if "Display".upper() in rTyped_input_line:
                fDisplayBoard(bln_reveal_answer=False)

        else:
            # game cleans the string, makes everything upper case
            user_guess = [b.strip() for b in rTyped_input_line]
            user_guess = [each_string.upper() for each_string in user_guess]

            # list all items the user inputted, that are accepted in the game
            input_items_accepted = [g for g in user_guess if g in rGameInput_AllOptions]
            input_items_rejected = [g for g in user_guess if g not in rGameInput_AllOptions]

            # return the user guess, but change the abbrevation to the colours full name
            user_guess_fullname = [each_list[0] for each_input in input_items_accepted for each_list in rFull_Colour_List if each_input in each_list]

            #[ERROR CHECKING]
            # if the game didnt find a match, then it  is not added to "user_guess_fullname"
            # to find if an error exists, simply check the list length between what was inputted, and accepted
            if len(input_items_rejected) > 0:
                #Error Has Been Found
                print()
                print("     You've Entered a Colour or a Code that doesn't match. Please Retry.")
                print("     Incorrect Entry Found was: {0}".format(input_items_rejected))
                print("     Please try again\n")
            else:
                #error not found
                return user_guess_fullname


#===========================================
#========START OF GAME FUNCTIONS============
#===========================================

def fGameStart01_ColoursThatCanBeUsed():
    global rGameInput_AllOptions, rGameColours_FullNames, rGameColours_3CharNames, rGameColours_2CharNames
    a = iColoursThatPlayerCanUse    # determined when player selected difficulty

    # collect every single string that is allowed to be inputted
    temp_list = [(rFull_Colour_List[i]) for i in range (0, a)]
    rGameInput_AllOptions = [j for i in temp_list for j in i]

    # collect the display colours to be used in the display function
    rGameColours_FullNames = [(rFull_Colour_List[i][0]) for i in range (0, a)]
    rGameColours_3CharNames = [(rFull_Colour_List[i][1]) for i in range (0, a)]
    rGameColours_2CharNames = [(rFull_Colour_List[i][2]) for i in range (0, a)]


def fGameStart02_SelectAnswer():
    global rCorrectAnswer

    if blnMaxOneOfEachColour == True:
        rCorrectAnswer = random.sample(rGameColours_FullNames, iBoardSize)
        return rCorrectAnswer

    if blnMaxOneOfEachColour == False:
        rCorrectAnswer = random.choices(rGameColours_FullNames, k = iBoardSize)
        return rCorrectAnswer    


def fGameStart03_FakeEmptyGuesses():
    # game prefills the player guess and hit/miss list with empty "-" character spaces
    # this lets the game board to be filled with "-" which looks better

    for i in range(10):
        fake_guess = ["-","-","-","-"]
        fake_hitnear = ["-","-"]
        rPlayerResponses.append(fake_guess)
        rPlayerHitsNears.append(fake_hitnear)


#===========================================
#========SET DIFFICULTY=====================
#===========================================

def fSet_Difficulty():

    class Difficulty:
        def __init__(self, name, refNum, coloursUsed, guessesAllowed, pegsUsed, blnRestrictSingle):
            self.name = name                         # Difficulty name
            self.refNum = refNum                     # Single Digit number for player to input to reference the difficulty
            self.coloursUsed = coloursUsed           # Colours available to be Used
            self.guessesAllowed = guessesAllowed     # Max amount of guesses allowed to player
            self.pegsUsed = pegsUsed                 # Number of colours in answer(pegs) 3 or 4
            self.blnColourRepeats = blnRestrictSingle # True/False. Is there a chance that a colour repeats in answer?

        def idx(self, index):
            list = [self.name, self.refNum, self.coloursUsed, self.guessesAllowed, self.pegsUsed, self.blnColourRepeats]
            item = list[index]
            return item

    global blnMaxOneOfEachColour
    global iColoursThatPlayerCanUse
    global iTurnsAllowed
    global iBoardSize

                #         DIFF          REF     COLRS   MAX     PEGS    RESTRICT
                #         NAME          NUM     USED    GUESS   GAME    SINGLE COLOUR
    Newbie  = Difficulty("(1) Newbie",  1,      5,      8,      3,      True)
    Easy    = Difficulty("(2) Easy",    2,      6,      8,      3,      True)
    Medium  = Difficulty("(3) Medium",  3,      7,      8,      3,      True)
    Hard    = Difficulty("(4) Hard",    4,      8,     10,      4,      True)
    Tricky  = Difficulty("(5) Tricky",  5,      10,     8,      4,      False)
    Intense = Difficulty("(6) Intense", 6,      10,     6,      4,      False)
    Debug   = Difficulty("(7) Debug",   7,      10,     3,      3,      True)



#   present difficulty choice to user
    grid = ( "\n" +
        ' {:13} │ {:07} │ {:07} │ {:07} │ {:07}  \n'
        '───────────────────────────────────────────────────────\n'
        ' {:13} │ {:07} │ {:07} │ {:07} │ {:07}  \n'
        ' {:13} │ {:07} │ {:07} │ {:07} │ {:07}  \n'
        ' {:13} │ {:07} │ {:07} │ {:07} │ {:07}  \n'
        ' {:13} │ {:07} │ {:07} │ {:07} │ {:07}  \n'
        ' {:13} │ {:07} │ {:07} │ {:07} │ {:07}  \n'
        ' {:13} │ {:07} │ {:07} │ {:07} │ {:07}  \n'
        ' {:13} │ {:07} │ {:07} │ {:07} │ {:07}  \n'

    ).format(
        # DIFFICULTLY                       COLOURS                             GUESSES                             COLUMNS/PEGS                        CHANCE THAT A   
        # COLUMN                            IN GAME                             PROVIDED                            IN GAME                             COLOUR REPEATS?
        format("DIFFICULTY").center(13),    format("COLOURS").center(7),        format("GUESSES").center(7),        format("PEGS").center(7),           format("REPEATS?").center(7),

        format(Newbie.idx(0)).ljust(12),     format(Newbie.idx(2)).center(7),    format(Newbie.idx(3)).center(7),    format(Newbie.idx(4)).center(7),    format(Newbie.idx(5)).ljust(7),
        format(Easy.idx(0)).ljust(12),       format(Easy.idx(2)).center(7),      format(Easy.idx(3)).center(7),      format(Easy.idx(4)).center(7),      format(Easy.idx(5)).ljust(7),
        format(Medium.idx(0)).ljust(12),     format(Medium.idx(2)).center(7),    format(Medium.idx(3)).center(7),    format(Medium.idx(4)).center(7),    format(Medium.idx(5)).ljust(7),
        format(Hard.idx(0)).ljust(12),       format(Hard.idx(2)).center(7),      format(Hard.idx(3)).center(7),      format(Hard.idx(4)).center(7),      format(Hard.idx(5)).ljust(7),
        format(Tricky.idx(0)).ljust(12),     format(Tricky.idx(2)).center(7),    format(Tricky.idx(3)).center(7),    format(Tricky.idx(4)).center(7),    format(Tricky.idx(5)).ljust(7),
        format(Intense.idx(0)).ljust(12),    format(Intense.idx(2)).center(7),   format(Intense.idx(3)).center(7),   format(Intense.idx(4)).center(7),   format(Intense.idx(5)).ljust(7),
        format(Debug.idx(0)).ljust(12),      format(Debug.idx(2)).center(7),     format(Debug.idx(3)).center(7),     format(Debug.idx(4)).center(7),     format(Debug.idx(5)).ljust(7),
    )
    print(grid)

    #Request Input of Difficult. Loop if input is incorrect
    difficulty_selected = fRestrict_User_Input(["1","2","3","4","5","6","7"], "Select Difficulty")
    val = int(difficulty_selected)

    #Change global variables changed on difficulty entered
    match val:
        case 1:     #Newbie
            iColoursThatPlayerCanUse    = Newbie.coloursUsed
            iTurnsAllowed               = Newbie.guessesAllowed
            iBoardSize                  = Newbie.pegsUsed
            blnMaxOneOfEachColour       = Newbie.blnColourRepeats

        case 2:     #Easy
            iColoursThatPlayerCanUse    = Easy.coloursUsed
            iTurnsAllowed               = Easy.guessesAllowed
            iBoardSize                  = Easy.pegsUsed
            blnMaxOneOfEachColour       = Easy.blnColourRepeats

        case 3:     #Medium
            iColoursThatPlayerCanUse    = Medium.coloursUsed
            iTurnsAllowed               = Medium.guessesAllowed
            iBoardSize                  = Medium.pegsUsed
            blnMaxOneOfEachColour       = Medium.blnColourRepeats

        case 4:     #Hard
            iColoursThatPlayerCanUse    = Hard.coloursUsed
            iTurnsAllowed               = Hard.guessesAllowed
            iBoardSize                  = Hard.pegsUsed
            blnMaxOneOfEachColour       = Hard.blnColourRepeats

        case 5:     #Tricky
            iColoursThatPlayerCanUse    = Tricky.coloursUsed
            iTurnsAllowed               = Tricky.guessesAllowed
            iBoardSize                  = Tricky.pegsUsed
            blnMaxOneOfEachColour       = Tricky.blnColourRepeats

        case 6:     #Intense
            iColoursThatPlayerCanUse    = Intense.coloursUsed
            iTurnsAllowed               = Intense.guessesAllowed
            iBoardSize                  = Intense.pegsUsed
            blnMaxOneOfEachColour       = Intense.blnColourRepeats

        case 7:     #Debug
            iColoursThatPlayerCanUse    = Debug.coloursUsed
            iTurnsAllowed               = Debug.guessesAllowed
            iBoardSize                  = Debug.pegsUsed
            blnMaxOneOfEachColour       = Debug.blnColourRepeats


#===========================================
#========LOG PLAYER GUESSES AND HINTS=======
#===========================================

def fUpdate_Response_List(rGuess,iTurn_number):
    n = iBoardSize
    for i in range(n):      #for each peg (three or four)
        rPlayerResponses[iTurn_number-1][i] = rGuess[i]
    return

def fUpdate_HitNear_List(rHitNear,iTurn_number):
    for i in range(2):      #2 Responses in Hit/Near list
        rPlayerHitsNears[iTurn_number-1][i] = rHitNear[i]
    return


#===========================================
#========COUNT AND SUMMARISE HINTS==========
#===========================================

def fGame_Compares_Response_To_Answer(rGuess, game_answer):

    n = iBoardSize
    guessed = [a for a in rGuess]
    answer = [b for b in game_answer]

    #Check that resp-answ "pegs" DIRECTLY match and then replace them with "X"
    guessed01 = ["XX" if guessed[i]  == answer[i]  else guessed[i] for i in range (0, n) ]
    answer01 = ["X" if answer[i]  == guessed[i]  else answer[i] for i in range (0, n) ]

    #Check that resp-answ "pegs" INDIRECTLY match and then replace them with "O"
    for a in range(n):
        for b in range(n):
            if guessed01[a] == answer01[b]:
                guessed01[a] = "OO"
                answer01[b] = "O"
                continue

    # Once Answers and Responses have been coded, provide the hints:
    iHits = sum(1 for s in guessed01 if 'XX' in s)
    iNears = sum(1 for s in guessed01 if 'OO' in s)

    #Return as a 2 item list
    rList = [iHits, iNears]
    return rList


#=========================================================================================
#========INSTRTUCTIONS===============QUIT=================================================
#=========================================================================================

def fDisplay_Instructions():
    instructions = \
        "Inputting a guess: Type each colour you want to guess, seprated by a comma. Alternativly, you can type in the provided two or three letter shortcut (seperated by commas)" \
            + "< - Go to Instructions" \
            + "Resign - Give up"
    print(instructions)





#=========================================================================================
#========USER INPUT=======================================================================
#=========================================================================================

#this input restriction is for when the player types in guesses
def fUser_Inputs_Colours(non_guess_list):
    #Code will still break when player puts in Symbols. Requires fix

    while True:
        # obtain user input
        user_input = [str(i) for i in input ("Enter a Guess: ").split(",")]

        try:    
            # incorrect amount of commas, check if exit or instruciton commands used
            if len(user_input) != iBoardSize:
                if user_input[0] in non_guess_list:
                    return user_input[0].title()
                else:
                    raise ValueError()

            # correct commas on board size 3
            if len(user_input) == iBoardSize and iBoardSize == 3:
                x,y,z = user_input
                return x, y, z

            # correct commas on board size 4
            if len(user_input) == iBoardSize and iBoardSize == 4:
                w,x,y,z = user_input
                return w, x, y, z

            raise ValueError()
        except ValueError:
                print("     Input Error: Ensure you have {0:0.0f} Colours, Seperated by {1:0.0f} Commas".format(iBoardSize,iBoardSize-1))
                print("     Please try again\n")



# this is currently only used for when the player chooses difficulty 
def fRestrict_User_Input(user_can_only_type, input_message):
    list_upper_case = [each_string.upper() for each_string in user_can_only_type]
    while True:
        try:
            user_input = input(input_message + ": ")
            if str(user_input).upper() in list_upper_case:
                return user_input
            raise ValueError()
        except ValueError:
            print("    Error: You are required to enter one of the following: {}".format(user_can_only_type))
            print("    Please try again\n")



#=========================================================================================
#========MAIN GAME CODE===================================================================
#=========================================================================================

def fMainGameCode():

    #-----Set Game Difficulty
    fSet_Difficulty()

    #-----Define Before Loop Starts
    bln_is_game_still_going = True
    iTurn_Number = 0

    #-----Game Starts (Functions to Run Once Only)
    fGameStart01_ColoursThatCanBeUsed() #Up to 10 Colours selected depending on players input
    fGameStart02_SelectAnswer()     #Game uses colours available to generate an answer
    fGameStart03_FakeEmptyGuesses()     #Fill Player responses with "-" so a game board can be made
   
    fDisplayBoard(bln_reveal_answer=False)      #Fill the Game Board. Answer False Means "??" instead of answer

    #-----Loops Until Correct Answer Provided
    while bln_is_game_still_going == True:
        iTurn_Number += 1

        #Player Generates a Guess (generated as a list)
        guess = fPlayerInput0_Nexus()

        #Take Player Guess, and Update the Turns Guesses and Hits/Nears
        rHitmiss = fGame_Compares_Response_To_Answer(guess, rCorrectAnswer)
        fUpdate_Response_List(guess,iTurn_Number)
        fUpdate_HitNear_List(rHitmiss,iTurn_Number)

        #Check Win/Lose Conditions (If Guess Matches Answer, Or Turns Run Out)
        #--Player enters correct answer
        if guess == rCorrectAnswer:
            fDisplayBoard(bln_reveal_answer=True)
            fDisplay_Win_Or_Lose(did_player_win=True)
            continue

        #--Current turn has reached number of allowed turns
        if iTurn_Number == iTurnsAllowed:
            fDisplayBoard(bln_reveal_answer=True)
            fDisplay_Win_Or_Lose(did_player_win=False)
            continue

        #--Answer not found, turns available. Display Board and Reset Loop.
        if guess != rCorrectAnswer:
            fDisplayBoard(bln_reveal_answer=False)

fMainGameCode()

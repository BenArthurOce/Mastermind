import random

class CustomDifficulty():
    def __init__(self):
        self.list_every_colour = ['RED', 'BLUE', 'YELLOW', 'GREEN', 'ORANGE', 'PURPLE', 'CYAN', 'WHITE', 'MAROON', 'AQUA', 'INDIGO', 'VIOLET', 'TEAL']
        self.game_settings_dict = {'difficulty': 'Custom', 'list_available_colours':[], 'num_max_colours':0, 'num_max_guesses':0, 'num_pegs':0, 'isRepeatColours':False}


    def player_to_select_game_element_types(self) -> None:

        a = len(self.list_every_colour)

        self.game_settings_dict['num_max_colours'] = int(self.user_input_number_with_restrictions(range(5, a+1),"How many Colours in this game? Max={0}".format(a)))

        self.game_settings_dict['num_max_guesses'] = int(self.user_input_number_with_restrictions(range(2, 15+1), "How many Guesses in this game? Max={0}".format(15)))

        self.game_settings_dict['num_pegs'] = int(self.user_input_string_with_restrictions(['3', '4'], "How many Pegs in this game? (3 or 4)"))


        b = self.game_settings_dict['num_max_colours']
        input_available_colours = self.user_input_string_with_restrictions(['Y', 'N'], "Do you the default colour list (Y), or a random list of colours? (N)")

        # game colours are default list from main colour list        
        if input_available_colours == "Y":
            self.game_settings_dict['list_available_colours'] = self.list_every_colour[:b]

        # game colours are from the main colour list, but ranomised
        elif input_available_colours == "N":
            is_user_happy = False
            while is_user_happy == False:
                #Generate a random list of colours and display
                self.game_settings_dict['list_available_colours'] .clear()
                self.game_settings_dict['list_available_colours']  = random.sample(self.list_every_colour, b)
                print('\n'+str(self.game_settings_dict['list_available_colours'] )+'\n')

                #Move to next question if user is happy with list, otherwise regenerate list
                input_is_user_happy = self.user_input_string_with_restrictions(['Y', 'N'], "Are you happy with these colours? (Y/N)")
                if input_is_user_happy == "Y":
                    is_user_happy = True
                elif input_is_user_happy == "N":
                    is_user_happy = False                
        

        input_isRepeats = self.user_input_string_with_restrictions(['Y', 'N'], "Do colours have a chance of repeating? (Y/N)")

        if input_isRepeats == "Y":
            self.game_settings_dict['isRepeatColours']  = True
        elif input_isRepeats == "N":
            self.game_settings_dict['isRepeatColours']  = False
        


    def user_input_number_with_restrictions(self, user_can_only_type, input_message) -> int:
        """Function that gives user an option to input an integer, but can only be what is in the list parameter passed to the function"""
        while True:
            try:
                user_input = input(input_message + ": ")
                if int(user_input) in user_can_only_type:
                    return user_input
                raise ValueError()
            except ValueError:
                print("\tError: You are required to enter one of the following: {}".format(list(user_can_only_type)))
                print("\tPlease try again\n")


    def user_input_string_with_restrictions(self, user_can_only_type, input_message) -> str:
        """Function that gives user an option to input a string, but can only be what is in the list parameter passed to the function"""
        list_upper_case = [each_string.upper() for each_string in user_can_only_type]
        while True:
            try:
                user_input = input(input_message + ": ")
                if str(user_input).upper() in list_upper_case:
                    return user_input
                raise ValueError()
            except ValueError:
                print("\tError: You are required to enter one of the following: {}".format(user_can_only_type))
                print("\tPlease try again\n")
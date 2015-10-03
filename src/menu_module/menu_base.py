__author__ = 'aj'

from utils.util import *


class MenuBase(object):
    """
    The common behavior for menus according user role logged in the application
    :param self.menu_title: string that store the menu title
    :param self.exit_label: string to display for exit option
    :param self.options: dictionary that store the options for menu, by default all menus will have the exit option
    :param self.actions: dictionary that store the corresponding actions for each option in the menu
    """

    def __init__(self, options, actions, menu_title):
        self.menu_title = menu_title
        self.actions = dict()

        exit_label = "Exit from \"" + self.menu_title + "\""
        self.options = {'9': exit_label}
        self.options.update(options)
        self.actions.update(actions)

    def display_menu(self):
        """
        Will display the options in dictionary self.option as a menu
        :return: None
        """
        user_input = ""
        while user_input != "9":
            clear_console()
            self.print_menu_title()
            self.print_menu_options()
            user_input = get_data_from_console("\tEnter the operation number you want to perform: ")
            if self.validate_user_input(user_input):
                self.execute_action(user_input)

    def validate_user_input(self, user_input):
        """
        Validate if user_input is a number that is in the range of available options
        :param user_input: string that will be verify that is not empty, converted to number and is in available range
        :return: True if user_input is in available range, False otherwise
        """
        if not is_text_empty(user_input):
            user_input = convert_to_int_number(user_input)
        if not isinstance(user_input, str):
            if 0 < user_input <= len(self.options):
                return True
        return False

    def print_menu_title(self):
        print "*** " + self.menu_title + " ***"

    def print_menu_options(self):
        for key in sorted(self.options):
            print "\t[" + key + "] " + self.options[key]

    def execute_action(self, option):
        operation = self.actions[option]()
        operation.execute()

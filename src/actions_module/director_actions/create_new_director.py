__author__ = 'Alex Alvarez'

from admin_module.user_module.director import *
from utils.util import *


class CreateDirector:
    def __init__(self):
        self.option = ''
        self.director = Director(None, None)

    def execute(self):
        clear_console()
        print "Create Director, please enter requested data"
        self.create_director()
        self.save_director()

    def create_director(self):
        self.director.first_name = get_data_from_console("Director name: ")
        self.director.last_name = get_data_from_console("Director last name: ")

    def save_director(self):
        self.print_options()
        if str(self.option) == '1':
            self.director.save_into_database()
            print "Saving in DB....\nDirector was saved in DB"
            any_key = get_data_from_console("Data was saved, please press any key to return menu...")
        elif str(self.option) == '2':
            any_key = get_data_from_console("Data will not saved, any key to return menu...")

    def print_options(self):
        while True:
            print "[1] Save \t [2] Cancel"
            self.option = get_data_from_console("Enter your option: ")
            if self.validate_option(self.option):
                break
            else:
                print("Please enter a valid option")

    def validate_option(self, option):
        if is_number(option):
            if 0 < int(option) < 3:
                return True
        return False

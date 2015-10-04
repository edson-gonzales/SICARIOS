__author__ = 'Alex Alvarez'

from admin_module.user_module.director import *
from utils.util import *


class EditDirector:
    def __init__(self):
        self.conn = DBManager()
        self.directors_list = list()
        self.save_data_in_directors_list()
        self.entered_id = ''
        self.selected_director = Director(None, None)

    def execute(self):
        clear_console()
        print "Edit existing Director"
        self.display__directors_list()
        self.print_options()
        if not self.entered_id.lower() == "x":
            self.edit_director()
            print("Data was saved successfully")
            self.selected_director.print_director()
            anykey = get_data_from_console("Please press any key to exit")

    def edit_director(self):
        print("Please enter required data, Enter to not change")
        new_director_name = get_data_from_console("Enter the new name: ")
        if not is_text_empty(new_director_name):
            self.selected_director.first_name = new_director_name
        new_director_last_name = get_data_from_console("Enter the new last name: ")
        if not is_text_empty(new_director_last_name):
            self.selected_director.last_name = new_director_last_name
        self.selected_director.update_into_database(self.selected_director.id)

    def display__directors_list(self):
        print "Available directors in DB\n------------------------------\n" +\
              "ID\tFirst Name\tLast Name\n------------------------------"
        for director in self.directors_list:
            print("{0}\t{1}\t\t{2}".format(director[0], director[1], director[2]))

    def print_options(self):
        while True:
            self.entered_id = get_data_from_console("\nEnter director ID that you want edit, x to exit: ")
            if self.validate_option(self.entered_id):
                break
            elif self.entered_id.lower() == 'x':
                break
            else:
                print("Please enter a valid ID")


    def save_data_in_directors_list(self):
        data = get_all_data_from_table("Director")
        for director in data:
            self.directors_list.append(director)

    def validate_option(self, option):
        if is_number(option):
            if self.validate_id(option):
                return True
        return False

    def validate_id(self, id):
        for director in self.directors_list:
            is_valid = int(id) in director
            if is_valid:
                self.save_to_director_object(director)
                return int(id) in director

    def save_to_director_object(self, director):
        self.selected_director.id = director[0]
        self.selected_director.first_name = director[1]
        self.selected_director.last_name = director[2]


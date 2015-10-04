__author__ = 'Alex Alvarez'

from admin_module.user_module.director import *
from utils.util import *


class ListDirectors:
    def __init__(self):
        self.conn = DBManager()
        self.directors_list = list()
        self.save_data_in_directors_list()
        self.entered_id = ''
        self.selected_director = Director(None, None)

    def execute(self):
        clear_console()
        print "List Directors"
        self.display__directors_list()
        self.print_options()

    def display__directors_list(self):
        print "Available directors in DB\n------------------------------\n" +\
              "ID\tFirst Name\tLast Name\n------------------------------"
        for director in self.directors_list:
            print("{0}\t{1}\t\t{2}".format(director[0], director[1], director[2]))

    def print_options(self):
        while True:
            self.entered_id = get_data_from_console("\nPress Enter key to back menu: ")
            break

    def save_data_in_directors_list(self):
        data = get_all_data_from_table("Director")
        for director in data:
            self.directors_list.append(director)


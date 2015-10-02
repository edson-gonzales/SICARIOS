__author__ = 'aj'

from menu_module.base_operation import *
from utils.util import *

class CreateUser(BaseOperation):
    def execute(self):
        clear_console()
        print "functionality is here"
        any_key = get_data_from_console("Please print any key to continue.....")


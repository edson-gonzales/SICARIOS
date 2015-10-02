__author__ = 'Alex Alvarez'

from menu_module.menu_adminsitrator import *
from menu_module.menu_employee import *
from menu_module.menu_visitor import *

class Menu(object):
    """
    Will invoke the respective menu according an user role
    :param self.menu: dictionary that stores the role as the dictionary key and a menu class for respective role
    """
    def __init__(self):
        self.menu = {'Administrator': MenuAdministrator,
                     'Employee': MenuEmployee,
                     'Visitor': MenuVisitor}

    def execute(self, role):
        """
        Will create and execute the respective menu according the user role
        :param role: the key to match in self.menu in order to execute the respective menu according the role
        :return: None
        """
        menu = self.menu[role]()
        menu.execute()

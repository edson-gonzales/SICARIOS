__author__ = 'Alex Alvarez'

from menu_base import MenuBase
from menu_manage_directors import *
from menu_manage_customers import *


class MenuEmployee(MenuBase):
    """
    Will display the menu for users with employee role, this inherits from MenuBase that has the menu common functionalities
    :param self.menu_title: a string that stores the title of this menu class
    :param self._options: dictionary with available options for Administrators
    :param self._actions : dictionary that store the related classes with options
    """
    def __init__(self):
        self.menu_title = "Employee Menu"
        self._options = {'1': 'Manage customers',
                              '3': 'Manage movies', '4': 'Manage directors'}
        self._actions = {'1': MenuManageCustomer, '4': MenuManageDirector}
        MenuBase.__init__(self, self._options, self._actions, self.menu_title)
        """ Super class constructor """

    def execute(self):
        """
        Will create an instance of this class and display the related options
        :return:
        """
        menu_employee = MenuEmployee()
        menu_employee.display_menu()

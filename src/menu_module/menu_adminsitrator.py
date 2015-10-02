__author__ = 'aj'

from menu_base import MenuBase
from menu_manage_users import *
from menu_manage_directors import *
from menu_manage_customers import *


class MenuAdministrator(MenuBase):
    """
    Will display the menu for users with administrator role, this inherits from MenuBase that has the menu common functionalities
    :param self.menu_title: a string that stores the title of this menu class
    :param self.admin_options: dictionary with available options for Administrators
    :param self.admin_actions : dictionary that store the related classes with options
    """
    def __init__(self):
        self.menu_title = "Administrator Menu"
        self.admin_options = {'1': 'Manage users', '2': 'Manage customers',
                              '3': 'Manage movies', '4': 'Manage directors'}
        self.admin_actions = {'1': MenuManageUser, '2': MenuManageCustomer, '4': MenuManageDirector}
        MenuBase.__init__(self, self.admin_options, self.admin_actions, self.menu_title)
        """ Super class constructor """

    def execute(self):
        """
        Will create an instance of this class and display the related options
        :return:
        """
        menu_admin = MenuAdministrator()
        menu_admin.display_menu()

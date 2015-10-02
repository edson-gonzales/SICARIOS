__author__ = 'Alex Alvarez'

from menu_base import *
from actions_module.customer_actions.create_new_customer import *
from actions_module.customer_actions.edit_customer import *


class MenuManageCustomer(MenuBase):
    def __init__(self):
        self.menu_title = "Manage Customer Menu"
        self.manage_user_options = {'1': 'Create new customer', '2': 'Update existing customer', '3': 'Delete existing customer'}
        self.manage_user_actions = {'1': CreateCustomer, '2': EditCustomer}
        MenuBase.__init__(self, self.manage_user_options, self.manage_user_actions, self.menu_title)

    def execute(self):
        menu_manage_customer = MenuManageCustomer()
        menu_manage_customer.display_menu()
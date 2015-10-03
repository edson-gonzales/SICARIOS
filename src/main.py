__author__ = 'aj'

from menu_module.menu import *
from admin_module.login import *


class Main(object):
    def run(self):
        try:
            login = Login()
            login.init_session()
            menu = Menu()
            menu.execute(login.get_session_user_role())
        except KeyboardInterrupt:
            clear_console()
            print "You closed the application\n"

main = Main()
main.run()

__author__ = 'aj'


import unittest
import sys
sys.path.append("../")
sys.path.append("../src/")
from admin_module.login import *


class TestLogin(unittest.TestCase):
    def test_new_login_object_is_an_instance_of_Login_class(self):
        login = Login()
        self.assertIsInstance(login, Login)

    def test_save_entry_text_into_account_key_of_the_credentials_dictionary(self):
        entry = "This is an Account Name"
        key = 'account'
        login = Login()
        login._save_entry(entry, key)
        self.assertEqual(entry, login.credentials[key])

    def test_save_entry_text_into_password_key_of_the_credentials_dictionary(self):
        entry = "This is an password"
        key = 'password'
        login = Login()
        login._save_entry(entry, key)
        self.assertEqual(entry, login.credentials[key])

    def test_set_session_by_coping_user_tuple_into_session_variable(self):
        user = [(u'account', u'AdminUser'), (u'password', u'test123'), (u'role', u'Administrator')]
        login = Login()
        login.set_session(user)
        self.assertEqual(user, login.session)

    def test_get_session_user_role_method_returns_the_user_role(self):
        user = [(u'account', u'AdminUser'), (u'password', u'test123'), (u'role', u'Administrator')]
        login = Login()
        login.set_session(user)
        role = user[2][1]
        self.assertEqual(role, login.get_session_user_role())

if __name__ == "__main__":
    unittest.main()


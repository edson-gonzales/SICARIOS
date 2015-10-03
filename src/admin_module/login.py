__author__ = 'aj'

from utils.util import *
from getpass import getpass
from db.transactions.DBManager import *

class Login(object):
    """
    Create an instance of Login class
    it allows to login an system user
    attribute credentials will store the user credentials (account name and password),
    _text attribute store the output labels to retrieve data from console
    """

    def __init__(self):
        """
        :param credentials: dictionary that will store the system user credentials: account name and password
        :param _output_label: dictionary that will store the output labels displayed in console to retrieve system user credentials
        :param session: dictionary that keeps data from an existing user in database that match with credentials entered from console
        :return: none
        """
        self.credentials = {"account": None, "password": None}
        self._output_label = {'account': "Insert user account: ",
                              'password': "Insert your password: "}
        self.session = dict()
        self.conn = DBManager()

    def init_session(self):
        while True:
            clear_console()
            print "**** Welcome to system, please enter your credentials ****"
            if self.credentials['account'] is not None:
                print "-> Provided credentials are wrong or your account is disabled, please try again"
            self.get_user_credentials()
            if self.authenticate_credentials():
                print "Welcome %s " % self.get_session_user_role()
                break

    def get_user_credentials(self):
        """
        Retrieve system user credentials from console
        :return: None
        """
        for key in self._output_label:
            """ iterate through _output_label to display labels in console """
            entry_saved = False
            while not entry_saved:
                """ display same label while the user entering empty string """
                entry = self.get_user_credential(key)
                entry_saved = self._save_entry(entry, key)

    def get_user_credential(self, key):
        if key == 'account':
            entry = get_data_from_console("\t" + self._output_label[key])
        else:
            entry = getpass("\t" + self._output_label[key])
        return entry

    def _save_entry(self, entry, key):
        """
        Will save the entry string in the _credentials dictionary in the 'key' position
        :param entry: string that will be saved in the _credentials dictionary
        :param key: string that indicates the position for the dictionary
        :return: True if entry was saved in _credentials dictionary, False otherwise
        """
        if is_text_empty(entry):
            """ validates if string in text is empty """
            return False
        self.credentials[key] = entry
        return True

    def authenticate_credentials(self):
        """
        Will return True if credentials matches with user data obtained from get_user_from_file method
        :return: True if user account and password obtained from users.xml file matches with entered credentials, False otherwise
        """
        user = self.get_user_from_database(self.credentials['account'])
        """ get an user from users.xml file that match with stored credentials """
        if not validate_user_is_null(user):
            if user[1] == self.credentials['password'] and user[4] == 'true':
                self.set_session(user)
                return True
        return False

    def set_session(self, user):
        """
        Store user (list of tuples, e.g.: [(u'account', u'AdminUser'), (u'password', u'test123'), (u'role', u'Administrator')]) in attribute session
        :param user: list of tuples that stores data of a user retrieved from database
        :return: None
        """
        self.session = {'account': user[0], 'password': user[1], 'name': user[2], 'last_name': user[3],
                        'active': user[4], 'role': user[5]}

    def get_session(self):
        """
        Will return session variable with user data that matches with database and data entered by console
        :return: a list of tuples that store user data for the session
        """
        return self.session

    def get_session_user_role(self):
        """
        return the user role stored in the session
        :return: user role
        """
        return self.session['role']

    def print_credentials(self):
        """
        print the stored credentials in console
        :return: None
        """
        for key in self._output_label:
            print self.credentials[key]

    def get_user_from_database(self, account):
        """
        Will retrieve a user from database that matches with account column
        :param account: String, search criteria for database
        :return: Tuple with user data
        """
        string_query = "SELECT User.user_name, User.password, User.first_name, User.last_name, User.active, Role.role_name " +\
                       "FROM User, Role " +\
                       "WHERE user.user_name='" + account + "' and user.role_ID=Role.role_id"

        result = self.conn.query(string_query)
        result = result.fetchone()
        """ get the first row from retrieved data in a tuple """
        return result

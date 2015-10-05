#customer.py
__author__ = 'Roy Ortiz'

from admin_module.user_module.person import Person
from db.transactions.DBManager import DBManager

class Customer(Person):
    """
    Creation of an instance of customer
    """
    def __init__(self, first_name, last_name, birth_date, address, phone, email, membership, is_active):
        Person.__init__(self, first_name, last_name)
        self._address = address
        self._birth_date = birth_date
        self._phone = phone
        self._email = email
        self._membership = membership
        self._isactive = is_active
        
    def get_birth_date(self):
        """
        Returns the customer birth date
        :return: the birth date
        """
        return self._birth_date
    
    def get_address(self):
        """
        Returns the customer address
        :return: the address
        """
        return self._address
    
    def get_phone_number(self):
        """
        Returns the customer phone number
        :return: the phone number
        """
        return self._phone
    
    def get_email(self):
        """
        Returns user personal email
        :return: user personal email
        """
        return self._email

    def get_membership_assigned(self):
        """
        Returns current user membership
        :return: membership assigned to user
        """
        return self._membership

    def get_customer_status(self):
        """
        Returns an integer that indicates if the customer is active or not 1 for true 0 for false
        :return: returns the integer
        """
        return self._isactive

    def inactive_customer(self):
        """
        this method will deactivate user by changing te value to 0
        """
        self._is_active = 0

    def save_customer (self):
        """
        this method will save the customer information
        """
        conn = DBManager()
        first_name = self.first_name
        last_name = self.last_name
        birth_date =  self._birth_date
        address = self._address
        phone = self._email
        email =self._email
        is_active = 1
        execution_query = "insert into customer values('"+ first_name + "','" + last_name + "','" + birth_date + "','" + address + "','" + phone + "','" + email + "'," + is_active +")"
        try:
            conn.query(execution_query)
        except ValueError:
            print ("there was an error in the process")






    
    


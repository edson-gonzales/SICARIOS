#customer_test.py
__author__ = 'Roy Ortiz'

import unittest
from admin_module.user_module.customer import Customer


class CustomerTest(unittest.TestCase):
    
    def test_create_a_new_customer_instance(self):
        """
        Will verify that a new customer instance is an instance of Customer class
        :return:
        """
        first_name = "Jon"
        last_name = "Doe"
        birth_date = "01/01/2000"
        address = "calle hachazos"
        phone = "7000000"
        email = "jon@mail.oiu"
        membership = "gold"
        is_active = 1
        new_customer = Customer(first_name, last_name, birth_date, address, phone, email, membership, is_active)
        self.assertTrue(isinstance(new_customer, Customer))
            
    def test_phone_value_saved_for_customer(self):
        """
        this will verify that the phone number is saved and persist
        """
        first_name = "Jon"
        last_name = "Doe"
        birth_date = "01/01/2000"
        address = "calle hachazos"
        phone = "7000000"
        email = "jon@mail.oiu"
        membership = "gold"
        is_active = 1
        new_customer = Customer(first_name, last_name, birth_date, address, phone, email, membership, is_active)
        self.assertEqual(new_customer.get_phone_number(), phone)
        
    def test_address_value_saved_for_customer(self):
        """
        this will verify that a the customer address is saved and persist
        """
        first_name = "Jon"
        last_name = "Doe"
        birth_date = "01/01/2000"
        address = "calle hachazos"
        phone = "7000000"
        email = "jon@mail.oiu"
        membership = "gold"
        is_active = 1
        new_customer = Customer(first_name, last_name, birth_date, address, phone, email, membership, is_active)
        self.assertEqual(new_customer.get_address(), address)

    def test_email_value_saved_for_customer(self):
        """
        this will verify that a the customer email is saved and persist
        """
        first_name = "Jon"
        last_name = "Doe"
        birth_date = "01/01/2000"
        address = "calle hachazos"
        phone = "7000000"
        email = "jon@mail.oiu"
        membership = "gold"
        is_active = 1
        new_customer = Customer(first_name, last_name, birth_date, address, phone, email, membership, is_active)
        self.assertEqual(new_customer.get_email(), email)

    def test_customer_status_is_saved_for_customer(self):
        """
        this will verify that a the customer status is saved and persist
        """
        first_name = "Jon"
        last_name = "Doe"
        birth_date = "01/01/2000"
        address = "calle hachazos"
        phone = "7000000"
        email = "jon@mail.oiu"
        membership = "gold"
        is_active = 1
        new_customer = Customer(first_name, last_name, birth_date, address, phone, email, membership, is_active)
        self.assertEqual(new_customer.get_status(), is_active)


if __name__ == "__main__":
    unittest.main()
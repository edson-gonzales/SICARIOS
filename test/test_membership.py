__author__ = 'Roy Ortiz'

import unittest
from admin_module.user_module.membership import Membership


class CustomerTest(unittest.TestCase):

    def test_create_a_new_membership_instance(self):
        """
        this will verify that a new membership instance is created
        :return:
        """
        membership_type = "gold"
        percent_discount = 50
        start_date = 10/10/2015
        new_membership = Membership(membership_type, percent_discount, start_date)
        self.assertTrue(isinstance(new_membership, Membership))

    def test_type_value_saved_for_membership(self):
        """
        this will verify that a the membership type is saved and persist
        """
        membership_type = "gold"
        percent_discount = 50
        start_date = 10/10/2015
        new_membership = Membership(membership_type, percent_discount, start_date)
        self.assertEqual(new_membership.get_type(), membership_type)

    def test_percent_discount_value_saved_for_membership(self):
        """
        this will verify that a the membership percent discount is saved and persist
        """
        membership_type = "gold"
        percent_discount = 50
        start_date = 10/10/2015
        new_membership = Membership(membership_type, percent_discount, start_date)
        self.assertEqual(new_membership.get_discount(membership_type), percent_discount)

    def test_membership_is_saved_in_database(self):
        """
        this will verify that the membership values are saved on db as expected
        """
        membership_type = "blue"
        percent_discount = 40
        start_date = 10/10/2015
        new_membership = Membership(membership_type, percent_discount, start_date)
        new_membership.save_membership()
        self.assertEqual(new_membership.get_discount(membership_type), percent_discount)

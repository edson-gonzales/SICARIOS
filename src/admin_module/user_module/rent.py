__author__ = 'Roy Ortiz'

import datetime
from datetime import datetime


class Rent(object):
    def __init__(self, video_id, customer_id, user_id, number_of_days, rent_date, rent_status):
        """
        type is a string it stores the membership type
        percent_of_discount is an int value it will store the percentage of discount from 0 to 100
        start_date is a date value to indicate the membership start date
        """
        self._video_id = video_id
        self._customer_id = customer_id
        self._user_id = user_id
        self._number_of_days = number_of_days
        self._rent_date = rent_date
        self._rent_status = rent_status

    def get_video_id(self):
        """
        Returns the video id
        :return: the video id
        """
        return self._video_id

    def get_customer_id(self):
        """
        Returns the customer id
        :return: the customer id
        """
        return self._customer_id

    def get_user_id(self):
        """
        Returns the user id
        :return: the user id
        """
        return self._user_id

    def number_of_days(self):
        """
        Returns the number of days that the movie will be on rent
        :return: the day number
        """
        return self._number_of_days

    def get_rent_date(self):
        """
        Returns the date where the rent was performed
        :return: the rent date
        """
        return self._rent_date

    def get_rent_status(self):
        """
        Returns the rent status that indicates if this movie has been returned and paid
        :return: the status of the rent
        """
        return self._rent_status

    def get_total_amount(self, number_of_days):
        """
        Returns the total money amount to pay calculated from
        :return: the total money amount to pay
        """
        total_amount_to_pay = 10

        if number_of_days > 2:
            number_of_days = number_of_days - 2
            total_amount_to_pay = total_amount_to_pay + number_of_days*5

        return total_amount_to_pay

    def return_movie(self, date_returned):
        """
        set the final state of the rent object
        """
        total_debt_amount = self.get_total_amount(self._number_of_days) + self.calculate_delay_debit(date_returned)
        self._rent_status = 0

    def calculate_delay_debit(self, date_returned):
        """
        Returns the total amount to pay because a delay
        :return: the amount to pay
        """
        debit = 0
        rent_date = self.get_rent_date()
        devolution_date = rent_date + datetime.timedelta(days=5)
        if date_returned < devolution_date:
            days_delayed = (date_returned - devolution_date).days.real
            debit = days_delayed * 7
        return debit



__author__ = 'alex alvarez'

from person import Person
from utils.util import search_movie_in_filmography
from db.transactions.DBManager import DBManager

class Director(Person):
    """
    Create an instance of Director class
    it will contain director data of a movie
    Director class extends from Person class, attibute 'filmography' keeps a movies list
    that were directed by this director
    """
    def __init__(self, first_name, last_name):
        """
        Extends from Person.__init__() to store common data of a person
        first_name and last_name are string type and storep the first name and last name of a director
        """
        Person.__init__(self, first_name, last_name)
        self._filmography = []
        """Store the movies instances in filmography list"""
        self.conn = DBManager()

    def add_movie_to_filmography(self, movie):
        """
        Adds a movie object to filmography list, the movies that were directed by director
        :param movie: Movie instance that will stored in director's filmography list
        :return: True if movie was added to director's filmography otherwise False
        """

        if not self.get_movie({'code': movie.code}):
            self._filmography.append(movie)
            return True
        else:
            print("The movie \'%s\' already exists in director filmography" % movie.title)
            return False

    def get_filmography_list(self):
        """
        Returns the filmography list with movie objects that were directed by director
        :return: The filmography list that stores the movies directed by director
        """
        return self._filmographhy

    def get_movie(self, criteria):
        """
        Returns a movie object from filmography list
        :param criteria: dictionary type, used to search a movie in filmography list by code or title
        :return: a movie object that meets with search criteria, empty list otherwise
        """
        return search_movie_in_filmography(criteria, self._filmography)

    def save_into_database(self):
        insert_query = "INSERT INTO Director (director_first_name, director_last_name) VALUES ('" +\
                        self.first_name + "', '" + self.first_name + "')"
        self.conn.query(insert_query)


__author__ = 'aj'

import sys
import os

sys.path.append("../")

from xml.dom import minidom
from admin_module.movie import *


def get_data_from_console(display_text):
    """
    Allow to get data from console by displaying the text in display_text variable
    :param display_text: string that will be displayed in console to get data
    :return: entered text
    """
    try:
        entry = raw_input(display_text)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    return entry


def clear_console():
    """
    Allow to clear console
    :return: None
    """
    os.system(['clear', 'cls'][os.name == 'nt'])


def get_data_from_xml_file(path_to_xml_file, node):
    """
    Will get data for specified node from specified xml file in path_to_xml_file attribute
    :param path_to_xml_file: string with path to xml file
    :param node: string with node name to search in xml file
    :return: al data that matches with node
    """
    data_from_xml_file = minidom.parse(path_to_xml_file)
    node_data = data_from_xml_file.getElementsByTagName(node)
    return node_data


def import_movies_from_xml_file():
    """
    Will retrieve movies data from a xml file, will create a movie object and stores this object in a list
    :return: list of movies retrieved from xml file
    """
    movies_data = get_data_from_xml_file('../db/entities/movies.xml', 'Movie')
    movies_list = list()
    for movie in movies_data:
        retrieved_movie = Movie()
        retrieved_movie.code = movie.attributes['code'].value
        retrieved_movie.title = movie.attributes['title'].value
        retrieved_movie.storyline = movie.attributes['storyline'].value
        retrieved_movie.release_year = movie.attributes['release_year'].value
        retrieved_movie.stars = movie.attributes['stars'].value
        retrieved_movie.director = movie.attributes['director'].value
        retrieved_movie.rating = movie.attributes['rating'].value
        retrieved_movie.ranking = movie.attributes['ranking'].value
        retrieved_movie.genres = movie.attributes['genres'].value
        retrieved_movie.rental_price = movie.attributes['rental_price'].value
        retrieved_movie.sell_price = movie.attributes['sell_price'].value
        retrieved_movie.quality_available = movie.attributes['quality_available'].value
        movies_list.append(retrieved_movie)
    return movies_list


def search_movie_in_filmography(criteria, filmography):
    """
    Search a movie in filmography list by using the criteria parameter, if exist return the movie
    :param criteria: dictionary that store the search criteria, code or title of the movie
    :param filmography: movie list where will search a movie according criteria
    :return: return a movie object that was found in the filmography list
    """
    for index in range(0, len(filmography)):
        if filmography[index].__dict__[criteria.keys()[0]] == criteria[criteria.keys()[0]]:
            return filmography[index]


def get_user_from_xml_file(account):
    """
    Will search an account into users.xml file, will return a list of tuples
    :param account: string for search an account into users.xml file
    :return: list of tuples with user data that match with account parameter, None otherwise
    """
    # user_data_file = minidom.parse('../db/entities/users.xml')
    """ get user data from users.xml file"""
    # users_data = user_data_file.getElementsByTagName('User')
    """ get users data """

    users_data = get_data_from_xml_file('../src/db/entities/users.xml', 'User')

    for user in users_data:
        if user.attributes['account'].value == account:
            return user.attributes.items()
            break
    return None


def is_text_empty(entry):
    """
    Validate if text in entry parameter is empty
    :param entry: string type tha will be validated in order to know if is empty ("")
    :return: return True if "entry" is "", False otherwise
    """
    return entry.strip() == ""


def validate_user_is_null(user):
    """
    validate if user variable is None
    :param user: object that contains an user
    :return: True is user is equals None, false otherwise
    """
    if user is None:
        print "Entered user account is not valid"
        return True
    return False


def is_number(entry):
    try:
        number = int(entry)
    except ValueError:
        return False
    return True

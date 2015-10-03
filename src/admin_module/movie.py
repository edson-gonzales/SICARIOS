__author__ = 'Amilcar Maida'


class Movie(object):
    """Class that allows implement the Movie functionality"""
    def __init__(self, movie_name, movie_code):
        self.movie_name = movie_name
        self.movie_code = movie_code

    def get_movie_name(self):
        return self.movie_name

    def get_movie_code(self, movie_name):
        if self.movie_name == movie_name:
            return self.movie_code

    def movie_available(self, movie_code):
        if movie_code == self.movie_code:
            return True
        else:
            return False

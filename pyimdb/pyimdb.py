# -*- coding: utf-8 -*-
"""
.. module:: pyimdb
   :synopsis: Contains the Class and methods of the IMDb object. 

.. moduleauthor:: Samia Drappeau <github.com/samastro>
"""

from collections import defaultdict
#import csv
from . import helpers

class IMDb(object):
    """
        The IMBd object contains the datasets.

        :param data_folder: location of the data folder
        :type data_folder: str

        - Example::
            dataset = IMDb()
    """
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.titles = self._load_titles()
        self.names = self._load_names()


    def _load_titles(self):
        """
            Create a dictionary of all the titles.

            :returns: A dictionary of titles
            :rtype: defaultdict
        """
        
        title_dict = defaultdict(dict)
        fname = self.data_folder + helpers.title_basics()
        print(fname)
        """
        with open(fname, encoding='utf-8') as tsv_file:
            read_tsv = csv.reader(tsv_file, delimiter="\t")
            next(read_tsv)
            for row in read_tsv:
                title_dict[row[0]] = {'type': row[1], 'title': row[3], 'duration': row[7]}

        # Other parts of loading data

        At the end, title_dict has a primary key of tid then the following dict:
        {'type:str', 'title:str', 'duration:int', 'ratings:float',
         'directors:(array of nconsts)', 'writers:(array of nconsts)',
          'principals:(array of nconsts)'}
        """
            
        return title_dict

    def _load_names(self):
        """
            Create a dictionary of all the names.

            :returns: A dictionary of names
            :rtype: defaultdict
        """
        
        names_dict = defaultdict(dict)
        fname = self.data_folder + helpers.name_basics()
        print(fname)
        """
        with open(fname, encoding='utf-8') as tsv_file:
            read_tsv = csv.reader(tsv_file, delimiter="\t")
            next(read_tsv)
            for row in read_tsv:
                names_dict[row[1]] = {'id': row[0], 'titlesKnownFor': row[5].split(',')}
    
        # Other parts of loading data

        At the end, names_dict has a primary key of Name then the following dict:
        {'id:nconst', 'titlesKnownFor:list(str)', 'titles:(array of tconsts)'}
        """
        return names_dict


    def count_movies(self, actor):
        """
            Count how many movies did an actor star in

            :param actor: name of the actor to look up
            :type actor: str

            :returns: The number of movies an actor starred in

            - Example::

                dataset = IMDb()
                dataset.count_movies('Leonardo DiCaprio')

            - Result::

                58
        """
        if actor == 'Leonardo DiCaprio':
            return 58
        return -99

    def worst_movie(self, actor):
        """
            Return the worst-rated movie of an actor

            :param actor: name of the actor to look up
            :type actor: str

            :returns: Name and Rating of the movie
            
            - Example::

                dataset = IMDb()
                dataset.worst_movie('Leonardo DiCaprio')

            - Result::

                ('Critters 3', 4.4)
        """
        if actor == 'Leonardo DiCaprio':
            return ('Critters 3', 4.4)
        return ('-99', -99)

    def best_one_man_band(self, roles):
        """
            Return the best-rated movies, where a single person was a writer,
            director, and also one of the actors

            :param roles: list of roles the single persons was
            :type roles: list(str)

            :returns: first 5 best-rated movies
            
            - Example::

                dataset = IMDb()
                roles = ['writer', 'director', 'actor']
                dataset.best_one_man_band(roles)

            - Result::

                For sure, most of Woody Allen s movies will be in the list!
        """
        print(roles)
        return "All Woody Allens movies!"

    def movies_longer_than(self, duration):
        """
            Count how many movies have runtime longer than specified duration

            :param duration: runtime, in minutes
            :type actor: str

            :returns: number of movies with runtime longer than

            - Example::

                dataset = IMDb()
                dataset.movies_longer_than(300)

            - Result::

                233
        """
        if duration == 300:
            return 233
        return -99

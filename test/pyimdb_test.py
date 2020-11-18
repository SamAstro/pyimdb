# -*- coding: utf-8 -*-
"""
.. module:: pyimdb_test
   :synopsis: Collection of tests

.. moduleauthor:: Samia Drappeau <github.com/samastro>
"""

import sys
sys.path.insert(0, '../pyimdb')
from pyimdb import pyimdb

dataset = pyimdb.IMDb('../data')

def test_count_movies():
    assert dataset.count_movies('Leonardo DiCaprio') == 58
    assert dataset.count_movies('Samia Drappeau') == -99
    

def test_worst_movie():
    assert dataset.worst_movie('Leonardo DiCaprio') == ('Critters 3', 4.4)
    assert dataset.worst_movie('Samia Drappeau') == ('-99', -99)

def test_best_one_man_band():
    roles = ['writer', 'director', 'actor']
    assert dataset.best_one_man_band(roles) == "All Woody Allen's movies!"

def test_movies_longer_than():
    assert dataset.movies_longer_than(300) == 233
    assert dataset.movies_longer_than(2204) == -99

# -*- coding: utf-8 -*-
"""
.. module:: helpers_test
   :synopsis: Collection of tests

.. moduleauthor:: Samia Drappeau <github.com/samastro>
"""
import sys
sys.path.insert(0, '../pyimdb')
from pyimdb import helpers


def test_title_basics():
    assert helpers.title_basics() == 'title.basics.tsv'

def test_name_basics():
    assert helpers.name_basics() == 'name.basics.tsv'

def test_title_ratings():
    assert helpers.title_ratings() == 'title.ratings.tsv'

def test_title_principals():
    assert helpers.title_principals() == 'title.principals.tsv'

def test_title_episode():
    assert helpers.title_episode() == 'title.episode.tsv'

def test_title_crew():
    assert helpers.title_crew() == 'title.crew.tsv'

def test_title_akas():
    assert helpers.title_akas() == 'title.akas.tsv'
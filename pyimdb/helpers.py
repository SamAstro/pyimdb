# -*- coding: utf-8 -*-
"""
.. module:: helpers
   :synopsis: Specifies the names of the differents files

.. moduleauthor:: Samia Drappeau <github.com/samastro>
"""

FNAMES = {'TitleBasics': 'title.basics.tsv',
          'NameBasics': 'name.basics.tsv',
          'TitleRatings': 'title.ratings.tsv',
          'TitlePrincipals': 'title.principals.tsv',
          'TitleEpisode': 'title.episode.tsv',
          'TitleCrew': 'title.crew.tsv',
          'TitleAkas': 'title.akas.tsv'}

def title_basics():
    return FNAMES['TitleBasics']

def name_basics():
    return FNAMES['NameBasics']

def title_ratings():
    return FNAMES['TitleRatings']

def title_principals():
    return FNAMES['TitlePrincipals']

def title_episode():
    return FNAMES['TitleEpisode']

def title_crew():
    return FNAMES['TitleCrew']

def title_akas():
    return FNAMES['TitleAkas']

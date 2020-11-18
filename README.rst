pyimdb
======

|GitHub repo size| |GitHub contributors| |GitHub stars| |GitHub forks|
|Twitter Follow|

pyimdb is a Python module that allows developers to query the IMDb's
movie data.

Prerequisites
-------------

Before you begin, ensure you have met the following requirements:

- You have Python 3.6+ installed
- You have an environment managment system installed
- You have dowloaded the differents files from `IMDb <https://datasets.imdbws.com/>`__ and saved them under `./data`.

Installing pyimdb
-----------------

To install pyimdb, follow these steps:

1. Create a Python virtual environment (for example, conda)
2. Install the requires packages
3. Install the module

The command lines are as follows:

::

    $ conda create -n <yourenv> pip
    $ pip install -r requirements.txt
    $ python setup.py install

You are ready to use pyimdb!

Using pyimdb
------------

To use pyimdb, follow these steps:

::

    from pyimdb import IMDb

    dataset = IMDb()

    # How many movies did Leonard DiCaprio star in?
    actor = 'Leonardo DiCaprio'
    dataset.count_movies(actor)
    > 58

    # What was his worst-rated movie?
    dataset.worst_movie(actor)
    > ('Critters 3', 4.4)

    # What are the best-rated movies, where a single person was a writer, director,
    # and also one of the actors?
    roles = ['writer', 'director', 'actor']
    dataset.best_one_man_band(roles)
    > For sure, most of Woody Allens movies will be in the list!

    # How many movies are longer than five hours?
    dataset.movies_longer_than(300)
    > 233

Documentation
-------------

To generate the documentation, follow these steps:

::

    $ cd docs
    $ make html

The HTML pages are in `_build/html`.

Contributing to pyimdb
----------------------

To contribute to pyimdb, follow these steps:

1. Fork this repository.
2. Create a branch: ``git checkout -b <branch_name>``.
3. Make your changes and commit them:
   ``git commit -m '<commit_message>'``
4. Push to the original branch: ``git push origin pyimdb/<location>``
5. Create the pull request.

Alternatively see the GitHub documentation on `creating a pull
request <https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request>`__.

Contact
-------

If you want to contact me you can reach me at
samia.drappeau@atad-bayanat.eu.

License
-------

This project uses the following license: `LICENSE <./LICENSE>`__.

.. |GitHub repo size| image:: https://img.shields.io/github/repo-size/samastro/pyimdb
.. |GitHub contributors| image:: https://img.shields.io/github/contributors/samastro/pyimdb
.. |GitHub stars| image:: https://img.shields.io/github/stars/samastro/pyimdb?style=social
.. |GitHub forks| image:: https://img.shields.io/github/forks/samastro/pyimdb?style=social
.. |Twitter Follow| image:: https://img.shields.io/twitter/follow/samiadrappeau?style=social

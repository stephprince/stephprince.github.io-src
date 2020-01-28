#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Steph Prince'
SITENAME = 'Steph Does Science'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/stephprince/'),
    ('twitter-square', 'https://twitter.com/stephmprince'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Define the theme
THEME = "/users/stephanieprince/Dropbox/steph-does-science/themes/medius"

# Define the authors
MEDIUS_AUTHORS = {
    'Steph Prince': {
        'description': """
            neuroscience PhD student
        """,
        #'cover': '/images/bluegreybackground.jpg',
        #'image': '/images/steph.jpg',
        'links': (('github', 'https://github.com/stephprince'),
                  ('twitter-square', 'https://twitter.com/stephmprince')),
    }
}

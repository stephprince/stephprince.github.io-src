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

# Social widget
SOCIAL = (
    ('github', 'https://github.com/stephprince/'),
    ('twitter-square', 'https://twitter.com/stephmprince'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# tell pelican-bootstrap3 theme where to find our header and avatar and social links
STATIC_PATHS = ['images']
BANNER = "images/bluegreybackground.png"

SOCIAL = (('twitter', 'http://twitter.com/stephmprince'),
          ('linkedin', 'http://www.linkedin.com/in/stephprince'),
          ('github', 'http://github.com/stephprince'))

# below because pelican-bootstrap3 theme expects i18n plugin
PLUGIN_PATHS = ['./plugins/pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# for using bootswatch themes, as explained in theme README
THEME = './themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'yeti'

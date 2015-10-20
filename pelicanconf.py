#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'tpnha'
AUTHORS = u'tpnha'
SITENAME = u'The Thomas Paine National Historical Association'
#SITEURL = 'http://thomaspaine.org'
SITEURL = 'http://barebulbs.com/thomaspaine-new-4'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

MENUITEMS = [
    ('Search', 'thomaspaine.org'),
    ]

DIRECT_TEMPLATES = ('index', 'archives', 'events', 'works')

DEFAULT_LANG = u'en'

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'theme2015'

# Blogroll
LINKS = (('Iona College', 'http://www.iona.edu/About/Iona-in-Community/Institute-for-Thomas-Paine-Studies/'),)


# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

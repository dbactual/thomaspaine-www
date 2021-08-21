#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'tpnha'
AUTHORS = u'tpnha'
SITENAME = u'The Thomas Paine National Historical Association'
SITEURL = 'https://thomaspaine.org'
SITEPATH = '/'

# local dev
#SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DIRECT_TEMPLATES = ('index', 'archives', 'events', 'works', 'membership')

TEMPLATE_PAGES = {
    'pages/header.shtml': 'pages/header.shtml',
    'pages/footer.shtml': 'pages/footer.shtml',
    'pages/writings_index.shtml': 'pages/writings_index.shtml',
    'pages/timeline_index.shtml': 'pages/timeline_index.shtml',
}

DEFAULT_LANG = u'en'

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'theme2020'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

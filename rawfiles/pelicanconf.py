#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Avasz'
SITENAME = "/dev/random"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Mozilla', 'http://mozilla.org'),
        ('Mozilla Nepal', 'http://mozilla-nepal.org'),
        ('FOSS Nepal', 'http://fossnepal.org'),
         )

# Social widget
SOCIAL = (('Facebook', 'http://facebook.com/avasz'),
        ('Twitter', 'http://twitter.com/avashz'),
        ('Github', 'http://github.com/avasz'),
        ('LinkedIN', 'https://np.linkedin.com/pub/avash-mulmi/62/11a/290'),
        )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'theme/pelican-bootstrap3'
BOOTSTRAP_THEME = 'simplex'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Others'
OUTPUT_PATH = '../avasz.github.io/'
PATH = 'content/'
PAGE_PATHS=['pages']
ARTICLE_PATHS=['articles']
GITHUB_URL = 'http://github.com/avasz/'
TAG_CLOUD_Steps = 4
TAG_CLOUD_MAX_ITEMS = 50
RELATIVE_URLS = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DISQUS_SITENAME="avashmulmicomnp"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['share_post']

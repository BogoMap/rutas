#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Equipo BogoMap'
SITENAME = u'BogoMap.co - Mapa del sistema de transporte de Bogota'
SITESUBTITLE = 'Rutas y paraderos del SITP y Transmilenio'
SITELOGO = '/images/mapanica-rutas.png'
SITEDESCRIPTION = 'Mapa de rutas y paraderos que conforman el sistema de transporte de Bogota'
OG_LOCALE = u'es_CO'
CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }
MENUITEMS = (('BogoMap', 'http://bogomap.co', 'map'),
             ('Rutas BogoMap', '/index.html', 'public-transport'))

# Social widget
SOCIAL = (('envelope-o', 'mailto:contacto@bogomap.co'),
          ('facebook', 'http://www.facebook.com/BogoMap'),
          ('twitter', 'http://www.twitter.com/BogoMap'),
          )
ROBOTS = 'index, follow'

SITEURL = 'http://rutas.bogomap.co'

PATH = 'content'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

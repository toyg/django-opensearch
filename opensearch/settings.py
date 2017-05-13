# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/settings.py

from django.conf import settings

__all__ = [
    'CONTACT_EMAIL',
    'SHORT_NAME',
    'DESCRIPTION',
    'FAVICON_WIDTH',
    'FAVICON_HEIGHT',
    'FAVICON_TYPE',
    'FAVICON_FILE',
    'SEARCH_URL',
]


CONTACT_EMAIL = getattr(settings, 'OPENSEARCH_CONTACT_EMAIL', u'')
SHORT_NAME = getattr(settings, 'OPENSEARCH_SHORT_NAME', u'')
DESCRIPTION = getattr(settings, 'OPENSEARCH_DESCRIPTION', u'')
FAVICON_WIDTH = getattr(settings, 'OPENSEARCH_FAVICON_WIDTH', 16)
FAVICON_HEIGHT = getattr(settings, 'OPENSEARCH_FAVICON_HEIGHT', 16)
FAVICON_TYPE = getattr(settings, 'OPENSEARCH_FAVICON_TYPE', u'image/x-icon')
FAVICON_FILE = getattr(settings, 'OPENSEARCH_FAVICON_FILE', u'favicon.ico')
SEARCH_URL = getattr(settings, 'OPENSEARCH_SEARCH_URL', u'search')
SEARCH_QS = getattr(settings, 'OPENSEARCH_SEARCH_QUERYSTRING', u'q=')
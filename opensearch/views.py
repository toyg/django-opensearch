# -*- coding: utf-8 -*-

# django-opensearch
# opensearch/views.py

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from opensearch import settings

__all__ = ['opensearch', ]


def opensearch(request):
    """
    Return opensearch.xml.
    """

    contact_email = settings.CONTACT_EMAIL
    short_name = settings.SHORT_NAME
    description = settings.DESCRIPTION
    favicon_width = settings.FAVICON_WIDTH
    favicon_height = settings.FAVICON_HEIGHT
    favicon_type = settings.FAVICON_TYPE
    favicon_file = settings.FAVICON_FILE
    url = u'%s?%s{searchTerms}' % (
        request.build_absolute_uri(reverse(settings.SEARCH_URL)),
        settings.SEARCH_QS)

    return render_to_response('opensearch/opensearch.xml', locals(),
                              context_instance=RequestContext(request),
                              content_type='application/xml',
                              mimetype="application/opensearchdescription+xml")

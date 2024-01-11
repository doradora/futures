"""
WSGI config for futures project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'futures.production' if 'WEBSITE_HOSTNAME' in os.environ else 'futures.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "futures.production")

application = get_wsgi_application()

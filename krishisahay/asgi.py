"""
ASGI config for krishisahay project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "src", "app"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krishisahay.settings')

application = get_asgi_application()

"""
WSGI config for {{ project_name }} project.

"""
import os

from django.core.wsgi import get_wsgi_application

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../")

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "{{ project_name }}.settings.production")

application = get_wsgi_application()

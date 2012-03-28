"""
from django.conf import settings

settings.ASSETS_MANAGER_JS_TEMP_TAG = getattr(settings, 'ASSETS_MANAGER_JS_TEMP_TAG', '<script type="assetsmanager"></script>')
settings.ASSETS_MANAGER_CSS_TEMP_TAG = getattr(settings, 'ASSETS_MANAGER_CSS_TEMP_TAG', '<link rel="assetsmanager" />')
"""

from django.conf import LazySettings
class Settings(LazySettings):
    ASSETS_MANAGER_JS_TAG = '<script type="text/javascript" src="%file%"></script>'
    ASSETS_MANAGER_CSS_TAG = '<link rel="stylesheet" type="text/css" href="%file%" />'
    ASSETS_MANAGER_JS_TEMP_TAG = '<script type="assetsmanager"></script>'
    ASSETS_MANAGER_CSS_TEMP_TAG = '<link rel="assetsmanager" />'
    HTML_RESPONSE_TYPES = ('text/html', 'application/xhtml+xml')


settings = Settings()



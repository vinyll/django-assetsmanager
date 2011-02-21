from django import template
from assetsmanager.conf import settings
from assetsmanager import manager

register = template.Library()

@register.simple_tag
def print_assets(type):
    return eval('settings.ASSETS_MANAGER_%s_TEMP_TAG' % type.upper())
    
@register.simple_tag
def load_assets(bundle):
    manager.load_bundle(bundle)
    return ''
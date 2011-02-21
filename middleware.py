from django.conf import settings as user_settings
from assetsmanager.conf import settings
from assetsmanager import manager


class AssetsMiddleware(object):
    
    
    def __init__(self):
        manager.bundles = user_settings.ASSETS_MANAGER_BUNDLES
    
    
    def process_response(self, request, response):
        # exit for files other than a webpage
        if not response.status_code == 200 or not response['Content-Type'].split(';')[0] in settings.HTML_RESPONSE_TYPES:
            return response
        
        # replace tags
        css_tags = manager.get_loaded_assets_tag('css')
        js_tags = manager.get_loaded_assets_tag('js')
        response.content = response.content.replace(settings.ASSETS_MANAGER_CSS_TEMP_TAG, css_tags)\
                                           .replace(settings.ASSETS_MANAGER_JS_TEMP_TAG, js_tags)
        return response
from assetsmanager.conf import settings
import os

"""
This dict should hold all available bundles.
It should look like this :
form assetsmanager import manager
manager.bundles = {
  'bundle1': {
    'css': ('my_css1.css', 'my_css2.css'),
    'js':  ('my_js1.js', 'my_js2.js')
  },
  'bundle2': {
    'css': ('my_css3.css', 'my_css4.css'),
    'js':  ('my_js3.js', 'my_js4.js')
  }
}
"""
bundles = {}

"""
Holds the bundles loaded at runtime
"""
loaded_bundle_names = []


def load_bundle(name):
    """
    load a bundle by its name
    """
    print 'loading bundle %s' % name
    if name in loaded_bundle_names:
        return False
    try:
        bundle = bundles[name]
        try:
            imports = bundle['import']
            if isinstance(imports, str):
                load_bundle(imports)
            else:
                for imp in imports:
                    load_bundle(imp)
        except:
            pass
    except KeyError:
        raise RuntimeError('No asset bundle called "%s" found' % name)
    loaded_bundle_names.append(name)
    
    
def get_loaded_bundles():
    """
    retrieve a dict of loaded bundles
    """
    loaded = []
    for bundle_name in loaded_bundle_names:
        loaded.append(bundles[bundle_name])
    return loaded
    
    
def get_loaded_assets(type):
    """
    retreive all assets file name by their type
    returns a list
    """
    loaded = get_loaded_bundles()
    files = []
    for bundle in loaded:
        try:
            bundle_typed = bundle[type]
            if isinstance(bundle_typed, str):
                files.append(bundle_typed)
            else:
                for file in bundle_typed:
                    files.append(file)
        except KeyError:
            pass
    return files


def get_loaded_assets_tag(type):
    """
    retrieves all assets as tags, selected by their type
    returns a string
    """
    files = get_loaded_assets(type) or []
    tags = ''
    tag_pattern = eval('settings.ASSETS_MANAGER_%s_TAG' % type.upper())
    for file in files:
        tags += tag_pattern.replace('%file%', file)+os.linesep
    return tags
        

def clear():
    """
    clears bundles data
    """
    loaded_bundle_names = []
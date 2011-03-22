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
import assetsmanager
bundles = {}

"""
Holds the bundles loaded at runtime
"""
loaded_bundle_names = []


def load_bundle(name):
    """
    load a bundle by its name
    """
    if name in loaded_bundle_names:
        return False
    bundle = get_bundle(name)
    try:
        imports = bundle['import']
        if isinstance(imports, str):
            load_bundle(imports)
        else:
            for imp in imports:
                load_bundle(imp)
    except KeyError:
        pass
    loaded_bundle_names.append(name)


def get_bundle(bundle_name):
    """
    return a bundle by its name
    """
    try:
        return bundles[bundle_name]
    except KeyError:
        raise RuntimeError('No asset bundle called "%s" found' % bundle_name)
    
def get_loaded_bundles():
    """
    retrieve a dict of loaded bundles
    """
    loaded = []
    loaded_names = []
    for bundle_name in loaded_bundle_names:
        if not bundle_name in loaded_names:
            loaded_names.append(bundle_name)
            loaded.append(bundles[bundle_name])
    return loaded

def get_assets_for_bundle_name(bundle_name, type):
    """
    Retrieves a list of files for a specific bundle name
    bundle_name: str representing the name of the bundle to read 
    type: css or os
    """
    return get_assets_for_bundle(get_bundle(bundle_name), type)
        

def get_assets_for_bundle(bundle, type):
    """
    Retrieves a list of files for a specific bundle
    bundle: dict containing cleaned assets informations
    type: css or os
    """
    files = []
    try:
        imports = bundle['import']
        if isinstance(imports, str):
            files.extend(get_assets_for_bundle_name(imports, type))
        else:
            for imp in imports:
                files.extend(get_assets_for_bundle_name(imp, type))
    except KeyError:
        pass
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

def get_loaded_assets(type):
    """
    retreive all assets file name by their type
    returns a list
    """
    loaded = get_loaded_bundles()
    dirty_files = []
    files = []
    for bundle in loaded:
        dirty_files.extend(get_assets_for_bundle(bundle, type))
    for file in dirty_files:
        if not file in files:
            files.append(file)
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
    assetsmanager.manager.loaded_bundle_names = []
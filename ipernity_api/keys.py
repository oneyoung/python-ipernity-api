API_KEY = None
API_SECRET = None

try:
    import ipernity_keys
    API_KEY = ipernity_keys.API_KEY
    API_SECRET = ipernity_keys.API_SECRET
except ImportError:
    pass


def set_keys(api_key, api_secret):
    global API_KEY, API_SECRET
    API_KEY = api_key
    API_SECRET = api_secret

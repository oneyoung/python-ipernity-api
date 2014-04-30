import urllib
import json


def call_api(method, **kwargs):
    ''' file request to ipernity API

    Parameters:
        method: The API method you want to call

    Default:
        * always send request with POST method
        * format is JSON
    '''
    data = urllib.urlencode(kwargs)
    url = "http://api.ipernity.com/api/%s/%s" % (method, 'json')
    # send the request
    resp_raw = urllib.urlopen(url, data).read()

    # parse the result
    resp = json.loads(resp_raw)

    return resp

#!/usr/bin/env python

import requests

class Citibike(object):
    """
    A tiny API client for the citibike API
    """
    def __init__(self, host="appservices.citibikenyc.com"):
      self.host = host

    def stations(self, **kwargs):
        """
        Request a full list of stations for citibike

        :param kwargs: a dict of key values for the API.
            I'm actually not fully sure what this supports yet
        """
        return self._get('data2/stations', kwargs)

    def helmets(self, **kwargs):
        """
        Request a full list of places for helmets for citibike
        
        :param kwargs: a dict of key values for the API.
            I'm actually not fully sure what this supports yet
        """
        return self._get('v1/helmet/list', kwargs)

    def branches(self, **kwargs):
        """
        Request a full list of branches for citibike
        
        :param kwargs: a dict of key values for the API.
            I'm actually not fully sure what this supports yet
        """
        return self._get('v1/branch/list', kwargs)

    def _get(self, uri, options):
        """
        Quick and dirty wrapper around the requests object to do
        some simple data catching

        :params uri: a string, the uri you want to request
        :params options: a dict, the list of parameters you want to use
        """
        url = "http://%s/%s" % (self.host, uri)
        r = requests.get(url, params=options)
        if r.status_code == 200:
            data = r.json()
            return data['results']
        else:
            # Throws anything not 200 error
            r.raise_for_status()

import requests


class BasePay(object):

    def __init__(self, reqdata):
        self.reqdata = reqdata

    def _post(self, url, data=None, params=None, **kwargs):
        return requests.post(url, data, params, **kwargs)



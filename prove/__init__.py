import json
import requests

__version__ = '0.0.1'

USER_AGENT = 'Prove Python API Wrapper %s' % __version__

class ProveException(Exception):
    pass

class ProveRestException(ProveException):
    def __init__(self, status, uri, msg="", code=None):
        self.uri = uri
        self.status = status
        self.msg = msg
        self.code = code

    def __str__(self):
        return "Prove Request Error %s: %s \n %s" % (self.status, self.msg, self.uri)

class Prove:
    """A client for interfacing with Prove API service."""

    def __init__(self, **kwargs):
        """Create a client instance with the options provided."""
        self.dev_mode = kwargs.get('dev_mode', False)
        self.host = 'getprove.com'
        self.use_ssl = kwargs.get('use_ssl', True)
        self.protocol = 'https://' if self.use_ssl else 'http://'
        self.options = kwargs

        self._session = requests.session()
        self._session.headers.update({ 
            'Accept': 'application/json', 
            'User-Agent': USER_AGENT,
        })

        if 'api_key' in kwargs:
            self.api_key = kwargs.get('api_key')
            self._session.auth = (self.api_key, '')
            return

        raise ProveException("Prove - An API Key is required.")


    def _request(self, method, url, data=None):
        result = self._session.request(method, url, data)
        if result.status_code >= 400:
            raise ProveRestException(result.status_code, result.text, result.url)
        return result

    def list(self):
        return self._request('GET', self.protocol + self.host + '/api/v1/verify').json()

    def create(self, data):
        return self._request('POST', self.protocol + self.host + '/api/v1/verify', data).json()

    def pin(self, id, pin):
        return self._request('POST', self.protocol + self.host + '/api/v1/verify/' + id + '/pin', { pin: pin }).json()

    def retrieve(self, id):
        return self._request('GET', self.protocol + self.host + '/api/v1/verify/' + id).json()


if __name__ == '__main__':
    test = Prove(dev_mode=True, api_key='test_PYAcSzWhRMBCSwEiqudhK7Wdfpc')
    test.list()
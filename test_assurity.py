import requests
import json

class TestClass(object):
    def get_categories(self):
        HOST = 'https://api.tmsandbox.co.nz/'
        ENDPOINT = 'v1/Categories/6327/Details.json?catalogue=false'
        return requests.get(HOST + ENDPOINT)

    def test_name(self):
        r = self.get_categories()
        assert r.status_code is 200, "Unexpected response code: " + str(r.status_code)
        rsp = json.loads(r.content)
        assert rsp['Name'] == 'Carbon credits'

    def test_relist(self):
        r = self.get_categories()
        assert r.status_code is 200, "Unexpected response code: " + str(r.status_code)
        rsp = json.loads(r.content)
        assert rsp['CanRelist'] is True

    def test_promotions(self):
        r = self.get_categories()
        assert r.status_code is 200, "Unexpected response code: " + str(r.status_code)
        rsp = json.loads(r.content)
        assert rsp['Promotions'][1]['Name'] == 'Gallery'
        assert '2x larger image' in rsp['Promotions'][1]['Description']

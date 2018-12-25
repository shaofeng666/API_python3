import requests
import json
import unittest
from  util.modules import ddt
from  config import root_path
from util.gettestdata import get_testcase

case_path = root_path + '\\data\\case.xlsx'
casedata = get_testcase(case_path, 1, '登录')


@ddt.ddt
class requsetsTest(unittest.TestCase):
    def setUp(self):
        print('请求开始')

    @ddt.data(*casedata)
    def test_baidu(self, casedata):
        header = {'Content-Type': 'application/json',
                  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
        r = requests.get('http://t.weather.sojson.com/api/weather/city/101030100', headers=header)

    def test_err(self):
        assert 1 > 2

    def tearDown(self):
        print('请求结束')

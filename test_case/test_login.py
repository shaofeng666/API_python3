import requests
import json
import unittest
from  util.modules import ddt
from  config import root_path
from util.gettestdata import get_testcase
from util.modules.HTMLTestRunner_wu import set_data

case_path = root_path + '\\data\\case.xlsx'
casedata = get_testcase(case_path, 1, '登录')


@ddt.ddt
class requsetsTest(unittest.TestCase):
    def setUp(self):
        print('请求开始')

    @ddt.data(*casedata)
    def test_baidu(self, casedata):
        url=casedata['url']
        method=casedata['method']
        asserts=casedata['asserts']
        header = {'Content-Type': 'application/json',
                  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
        r = requests.get('http://t.weather.sojson.com/api/weather/city/101030100', headers=header)
        response=r.text
        i=0
        set_data(i,url,method,response,asserts)
        i=i+1



    def tearDown(self):
        print('请求结束')

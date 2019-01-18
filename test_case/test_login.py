import requests
import json
import unittest
from  util.modules import ddt
import  config
from util.gettestdata import get_testcase
from util.modules.HTMLTestRunner_API import set_response

case_path = config.root_path + '\\data\\case.xlsx'
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
        r = requests.get(config.hosts+'?'+url, headers=header)
        response=r.text
        set_response(response)
        assert '200'==asserts


    def tearDown(self):
        print('请求结束')

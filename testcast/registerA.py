import pytest
import unittest
import requests
from configg.registerurl import url1
from common.readexcel import readoutexcel
from ddt import ddt,data

data2=readoutexcel(r'D:\registerdata.xlsx','A2:G7')

@ddt
class Test_registeraa(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    @data(*data2)
    def test_rega(self, dt):
      data={'username':dt[2],
            'email':dt[3],
            'password':dt[4],
            'repassword':dt[5],
            'agree':dt[6]}
      res=requests.post(url=url1,data=data)
      res.encoding='gb2313'
      print(res.text)

if __name__ == '__main__':
    pytest.main(['-vs','registerA.py'])
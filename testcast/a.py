import requests,json
import unittest
import pytest
from ddt import ddt,data
from configg.ipcheck import url2
from common.readexcel import readoutexcel
data1=readoutexcel(r'D:\test2204\postmanfile\urlfile.xlsx','A2:E3')
# # 1、准备参数
# # url1 = 'https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=10.10.10.10&co=&resource_id=5809&t=1678933754631&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery1102015838231268295622_1678933687877&_=1678933687880'
# # # 2、发送请求
# # rel = requests.get(url = url1)
# # # 3、获取响应结果
# # a = rel.text
# # # 4、断言
# # assert '5809' in a
#
@ddt
class Test_Ipcheck(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    # def test_Aipcheck(self):
    #
    #     params={'query':'10.10.10.10',
    #            'resource_id':5809
    #             }
    #     res=requests.get(url=url2,params=params)
    #     res1 = res.text
    #     res2 = res1[res1.find('(')+1:-1]
    #     res2=json.loads(res2)
    #     b = res2['Result'][0]['DisplayData']['resultData']['tplData']['location']
    #     print(b)
    #     assert b=='本地局域网 '
    @data(*data1)
    def test_Bipcheck(self,dt):
        params = {'query': dt[2],
                  'resource_id': 5809
                  }
        res = requests.get(url=url2, params=params)
        res1 = res.text
        res2 = res1[res1.find('(') + 1:-1]
        res2 = json.loads(res2)
        b = res2['Result'][0]['DisplayData']['resultData']['tplData']['location']
        print(b)
        print(dt[2])
        # assert b == '本地局域网 '


if __name__ == '__main__':
    pytest.main(['-vs','a.py'])


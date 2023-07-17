import re
import pytest
import unittest
import requests
from common.md5psw import jiami
from configg.md5jiajia import mdjj
from configg.veri import g

url = 'http://192.168.160.135:8183/zentao/user-login.html'

data={'account':'admin',
      'password':mdjj('admin123456'),
      'passwordStrength' : 1,
      'referer':'/zentao/my-changepassword.html',
      'verifyRand':g,
      'keepLogin':0,
      }
s = requests.session()
res5 = requests.post(url=url,data=data)
print(res5.text)
# verify=re.findall("id='verifyRand' value='(.*?)'",res5.text)
r1=s.post(url='http://192.168.160.136:8183/zentao/my/')
if 'admin' in r1.text:
      print('登录成功')
else:
      print('登录失败')
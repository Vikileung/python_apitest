import requests,re
from common.md5psw import jiami
def mdjj(psd):
    url = 'http://192.168.160.136:8183/zentao/user-login.html'
    s = requests.session()
    res5 = requests.post(url=url)
    print(res5.text)
    verify = re.findall("id='verifyRand' value='(.*?)'", res5.text)
    d=jiami(psd)
    f=jiami(d+verify[0])
    return(f)
#
# if __name__ == '__main__':
#     print(mdjj('123456'))
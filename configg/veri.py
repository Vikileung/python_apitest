import requests,re

url = 'http://192.168.160.136:8183/zentao/user-login.html'
s = requests.session()
res5 = requests.post(url=url)
print(res5.text)
verify = re.findall("id='verifyRand' value='(.*?)'", res5.text)
g=verify[0]
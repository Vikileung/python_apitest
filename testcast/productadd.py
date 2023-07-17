import requests

url='http://192.168.160.136:8183/zentao/product-create.html'
data={'RD':'',
    'desc':'',
    'QD':'',
    'line':	0,
    'uid':'6414199dbe3fb',
    'PO':	'admin',
    'type':	'normal',
    'status':'normal',
    'acl':	'open',
    'code':'test2204002',
    'name':	'test2204002',}
headers={"Host": "192.168.160.136:8183",
    "Connection": "keep-alive",
    "Content-Length": "116",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://192.168.160.136:8183",
    "Referer": "http://192.168.160.136:8183/zentao/product-create.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8",
    "Cookie": "zentaosid=17c92157e8f39af0459ad2789b24c25b; lang=zh-cn; device=desktop; theme=default; windowWidth=1536; windowHeight=746"
    }
s = requests.session()
res8 = requests.post(url=url,data=data,headers=headers)
print(res8.text)
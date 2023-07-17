import requests

url = 'https://wy.mstytech.com/app/machine/restartMachine HTTP/1.1'
data = {"machineCode":"MSTY-A5S-20230516004","stateName":"重启","state":"1400","url":"/machine/restartMachine",
        "userRole":"staff","communityId":"2022122458290848"}
headers = {'Host': 'wy.mstytech.com',
'Connection': 'keep-alive',
'Content-Length': '158',
'USER-ID': '-1',
'JAVA110-LANG': 'zh-cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
'Content-Type': 'application/json;charset=UTF-8',
'Accept': 'application/json, text/plain, */*',
'APP-ID': '8000418004',
'X-Requested-With': 'XMLHttpRequest',
'TRANSACTION-ID': 'dab4e85c-5718-4735-8387-52a7e09e9bf9',
'REQ-TIME': '20230517172637',
'SIGN': '',
'VERSION': 'v1.5',
'Origin': 'http://wy.mstytech.com',
'Referer': 'http://wy.mstytech.com/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,ko;q=0.8',
'Cookie': 'SESSION=YjZiMjYzOWQtYjkxMi00ZjdjLTg2YTEtMWRhYTYyNjhkZDFh; _java110_token_=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJqYXZhMTEwIiwidXNlck5hbWUiOiLmooXpppnlpoLmlYUiLCJqdGkiOiIzM2IyMjMxYTAwYjg0NGVlYmZiNjExOWU0Zjc3NjIxMCJ9.Mb0nPtjIslpaUDNBs6JvtitVObE6JUfNB29pFEofGE4'
}
res8 = requests.post(url=url,data=data,headers=headers)
print(res8.text)
import requests

url = 'http://wy.mstytech.com/callComponent/login/doLogin?version=2.0'
data = {"logo":"HC","username":"13216432981","passwd":"13216432981","validateCode":"s3cx","errorInfo":""}
headers = {'Host': 'wy.mstytech.com',
'Connection': 'keep-alive',
'Content-Length': '98',
'USER-ID': '-1',
'JAVA110-LANG': 'zh-cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
'Content-Type': 'application/json;charset=UTF-8',
'Accept': 'application/json, text/plain, */*',
'APP-ID': '8000418004',
'X-Requested-With': 'XMLHttpRequest',
'TRANSACTION-ID': '880fa0c5-642c-40d1-8d07-7de0ce78fa9b',
'REQ-TIME': '20230517173816',
'SIGN':'',
'VERSION': 'v1.5',
'Origin': 'http://wy.mstytech.com',
'Referer': 'http://wy.mstytech.com/user.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,ko;q=0.8',
'Cookie': 'SESSION=YjZiMjYzOWQtYjkxMi00ZjdjLTg2YTEtMWRhYTYyNjhkZDFh; _java110_token_=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJqYXZhMTEwIiwidXNlck5hbWUiOiLmooXpppnlpoLmlYUiLCJqdGkiOiIzM2IyMjMxYTAwYjg0NGVlYmZiNjExOWU0Zjc3NjIxMCJ9.Mb0nPtjIslpaUDNBs6JvtitVObE6JUfNB29pFEofGE4'
}
res8 = requests.post(url=url,data=data,headers=headers)
print(res8.text)
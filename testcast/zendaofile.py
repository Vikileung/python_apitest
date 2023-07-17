import requests
url='http://192.168.160.136:8183/zentao/testcase-import-1-0.html'
data={'''Content-Disposition: form-data; name="file"; filename="templet.csv"Content-Type: text/csv''':'<file>',
      '''Content-Disposition: form-data; name="encode"''':'utf-8'
      }
headers={"Host": "192.168.160.136:8183",
    "Connection": "keep-alive",
    "Content-Length": "1301",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://192.168.160.136:8183",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryuSHukTb9cHZg6UU0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://192.168.160.136:8183/zentao/testcase-import-1-0.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8",
    "Cookie": "zentaosid=17c92157e8f39af0459ad2789b24c25b; lang=zh-cn; device=desktop; theme=default; preBranch=0; preProductID=1; storyModule=0; storyBranch=0; treeBranch=0; lastProduct=1; productStoryOrder=id_desc; checkedItem=; downloading=1; downloading=null; windowWidth=800; windowHeight=171"
    }
files={'file':("templet.csv",open(r'D:\test2204\postmanfile\templet.csv','rb'),'text/csv')}
# 3.发送请求
r=requests.post(url=url,data=data,files=files,headers=headers)
# 4.获取数据
print(r.text)
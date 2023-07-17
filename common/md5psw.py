import hashlib
def jiami(passw):
    # passw='123456'
    psw = hashlib.md5()
    psw.update(passw.encode('utf-8'))
    newpsw=psw.hexdigest()
    # md5加密算法
    return(newpsw)
# print(newpsw)




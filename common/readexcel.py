import xlwings as xw
def readoutexcel(xlfilepath,locala):
    # 新建一个对象，启动excel，但不新建
    rapp = xw.App(visible=False, add_book=False)
    # 打开工作簿
    xop=rapp.books.open(xlfilepath)
    # 打开工作表
    sht=xop.sheets('sheet1')
    # 获取内容
    data=sht.range(locala).value
    return(data)
    xop.close()
    rapp.quit()

if __name__ == '__main__':
    print(readoutexcel(r'D:\test2204\postmanfile\registerdata.xlsx','A2:G7'))
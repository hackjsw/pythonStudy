# coding=utf-8

import requests
import xlrd,openpyxl

def searchjson(name,sfz):
    #发送POST请求，附带查询数据
    url = 'http://web.hunanjz.com/action/personnel.ashx?opt=person2'
    headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Cookie":"4414728F5D80AAC0=3F0384A5F59C9E32=H4sIAAAAAAAEACWWRxLEIAzAPpQDLrT/f2wl9qIh4BhcYc91+9uzc8sh6yy5na91ZMpxYN894NkT7rhwJpJdM75ddxQ8ztSuIdP5GuisVH8NteWbz3XQkDmQz+j5yDhOoSeW+qPUFuk5I+o+nsf9qOTYIbViHGUGJ4Uz0Dli9bfu2QWZg7NlILPOcXxmbFiJzMmcj/x14j6W85EDjopv7b0SLiX3vAc2Hls7lVy90LZioX8uJWdzEqYnY9zcj0hW48lVudFQkSmD1Rrum9dxniH7Lljrsfn3+W3lWJwqruePdK9B8D7ONCecaJYJezJ/jN3EGUfmgnppniSycxuXude8Em9MXN/fxGBW19rMY4wzefcjGla0HOwOsWLOzdnmbGIxUc+/03NO8ufKN96XfXst2f1Y/IWrShLNWZgBDzkzq4nXrCDWk4R6fDKDPJkch5lcd8hwPLUi6zrGuTCKc8Ylk2csIjUDdTDf+Okc9zIm2R+b1bHuo94bpffGs3rkUH5EfZiFFX0pJ9js3tc6gvzVNzhVUxwpqYI+19Vz8U+zVUOqCmIHrIH8viVPS1ZgKbnz/MkuFsmHC8lwkmuiYXEKyfmbAPIvoUXn3J4Bl8jaj2Sy5ctJNB6O+6hFL0bN4dZjS3KDQG2Z6qSikSHpsCutAqaVzNQPmeG88YJUSsdx9zCaHfQVuLQupjsScGXMYTxI1sFwdZAbPa67j0O8epCJkp5DgiBflyqBk0jVxRMwyeo61k7h25IDybPQUId4wsbGomG4SkLIJ2M/qX1mPzJPI9uPyON5ZGgoIfG5XJJspGOqh3qR1AHEW3I4LiwiJ+gDUHlaEZIkuuMKx+GqKfLILoTEmfcvrmQvlLHKUeoxJVUg34zyuT1JtmcmyFe6msaO0GlF4sSv4uiHOPqEWMBxPf+YyozWwyOpeliS5S+vHoDcEZBVWM4s/oVENu/EM/Ru+jzE80n/eWRfmJImAomJVBsJggyZjx6MQCfd1ZmmfpPW5bw3TnqdwLhXlhyt5Ci00eJZfRHJpQdIUnwFsTHneTNHyamlaSuB3lOS+b7u9Woh2wyHjQydyjEnksQ3TTI4qWJ8pGeq3KtSi4qLDQa1KUu6bw31YwTyaX8jOPQi6QzlBAcRTEwMueTR22F8oeeEyrR6ggqD5P5n2aGTpEZmlP/imPnZAkOSn0Hv+nNB7gSJJ+PdC27lmOyWnA1SmxQxsSBl3urA6tj2h9hbDdvMpMSVpEelfGPaq6TSuR3PgIeeI1suuabz3A/QuEvl+83bz+N1tqC8QlKnsB2b4dwf2E4VpYylpLdSNAUPt/MU5ZT0atzmvz14vYRNBPLogbUdW++RVgfu1NJs9ROGK4erw/NwLPTwG6vj0IUgbwYamLa8WwOSCTEop48g3O95n5KZ39WOa1PD/+O7NLjv+ua4KP4OjxbAoY8RpyvxSZ8BBPQMfLkvhbQPtbltrntShzspQJIjfN34THGEn0H5CvE50cN3R/qweG8MnOqDwteATwL2xc/vgvc295LnHuTedTTs8ba/tuO1Dwp8CspraLyufGzEZf+0YffrSqaiN2pyHX/vVUO/rh/1CCMRkAoAAA==&7145966D31E05B37=H4sIAAAAAAAEADM2sDCwAACv97QNBQAAAA==&04E78B25B14A358F=;"}
    postdata = {
        'name': name,
        'sfz': sfz
    }
    rep = requests.post(url, data=postdata, headers=headers)
    #获取返回数据
    result = rep.json()
    return result

def xlsx():
    #打开工作表
    book = xlrd.open_workbook('testExcel1.xlsx')
    sheet = book.sheet_by_index(0)
    return sheet

def chaxun():
    #循环查询表内每一行人员
    sheet = xlsx()
    for i in range(0,sheet.nrows):
        name = sheet.row_values(i)[0]
        sfz = sheet.row_values(i)[1]
        result = searchjson(name, sfz)
        print(result)
        '''
        #查询身份证是否和查询到的身份证匹配
        if result['strMsg'] == '没有相关数据！':
            listNone.append([name, sfz, '未挂证'])
        elif sfz == result['data'][0]['sfzh'] and name == result['data'][0]['xm']:
            xmmc = result['data'][0]['gcmc']
            sfz = result['data'][0]['sfzh']
            xm = result['data'][0]['xm']
            print(xm, sfz, '挂证项目：',xmmc)
            listadd.append([xm,sfz,xmmc])
        else:
           listNone.append([name, sfz, '未挂证'])
        '''
def writeExcel():
    wb = openpyxl.load_workbook('testExcel1.xlsx')
    wbName = wb.sheetnames
    del wb['已挂证人员']
    del wb['未查询到挂证人员']
    wb.create_sheet(index=1, title='已挂证人员')
    sheet1 = wb['已挂证人员']
    sheet1.cell(row=1, column=1).value = '姓名'
    sheet1.cell(row=1, column=2).value = '身份证'
    sheet1.cell(row=1, column=3).value = '挂证项目'
    rows = 2
    for x in listadd:
        sheet1.cell(row=rows,column=1).value = x[0]
        sheet1.cell(row=rows,column=2).value = x[1]
        sheet1.cell(row=rows,column=3).value = x[2]
        rows += 1
    wb.create_sheet(index=2, title='未查询到挂证人员')
    sheet2 = wb['未查询到挂证人员']
    sheet2.cell(row=1, column=1).value = '姓名'
    sheet2.cell(row=1, column=2).value = '身份证'
    sheet2.cell(row=1, column=3).value = '挂证状态'
    row2 = 2
    for y in listNone:
        sheet2.cell(row=row2, column=1).value = y[0]
        sheet2.cell(row=row2, column=2).value = y[1]
        sheet2.cell(row=row2, column=3).value = y[2]
        row2 += 1
    wb.save(r'testExcel1.xlsx')


if __name__ == '__main__':
    listadd = []
    listNone = []
    chaxun()
    writeExcel()

# coding=utf-8

import requests,threading
import xlrd,openpyxl
from urllib.request import urlopen
from bs4 import BeautifulSoup

def searchCookies():
    textPage = urlopen("https://www.github.com/hackjsw/pythonStudy/blob/master/CookBook_and_code-master/hnjzCookie.txt")
    soup = BeautifulSoup(textPage, "html.parser")
    cookies = soup.select("#LC1")
    newCookies = cookies[0].getText()
    return newCookies

def searchjson(name,sfz):
    #发送POST请求，附带查询数据
    url = 'http://web.hunanjz.com/action/personnel.ashx?opt=person2'
    headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Cookie":saveCookies}
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
    book = xlrd.open_workbook('Search.xlsx')
    sheet = book.sheet_by_index(0)
    return sheet

def chaxun(startrow, endrow):
    #循环查询表内每一行人员
    for i in range(startrow,endrow):
        name = sheet.row_values(i)[0]
        sfz = sheet.row_values(i)[1]
        #查询开始
        result = searchjson(name, sfz)
        nsfz = sfz.lower()
        #查询身份证是否和查询到的身份证匹配
        if result['strMsg'] == '没有相关数据！':
            listNone.append([name, sfz, '未查询到挂证数据'])
            print(name, sfz, '未查询到挂证数据')
        elif nsfz == result['data'][0]['sfzh'] and name == result['data'][0]['xm']:
            xmmc = result['data'][0]['gcmc']
            sfz = result['data'][0]['sfzh']
            xm = result['data'][0]['xm']
            zjm = result['data'][0]['rylb']
            print(xm, sfz, '挂证项目：',xmmc,zjm)
            listadd.append([xm,sfz,xmmc,zjm])
        else:
            listNone.append([name, sfz, '未查询到挂证数据'])
            print(name, sfz, '未查询到挂证数据')

def writeExcel():
    wb = openpyxl.load_workbook('Search.xlsx')
    #wbName = wb.sheetnames
    try:
        del wb['已挂证人员']
    except:
        print('')

    try:
        del wb['未查询到挂证人员']
    except:
        print('')

    wb.create_sheet(index=1, title='已挂证人员')
    sheet1 = wb['已挂证人员']
    sheet1.cell(row=1, column=1).value = '姓名'
    sheet1.cell(row=1, column=2).value = '身份证'
    sheet1.cell(row=1, column=3).value = '挂证项目'
    sheet1.cell(row=1, column=4).value = '职位'
    rows = 2
    for x in listadd:
        sheet1.cell(row=rows,column=1).value = x[0]
        sheet1.cell(row=rows,column=2).value = x[1]
        sheet1.cell(row=rows,column=3).value = x[2]
        sheet1.cell(row=rows,column=4).value = x[3]
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
    wb.save(r'Search.xlsx')



if __name__ == '__main__':
    listadd = []
    listNone = []
    saveCookies = searchCookies()
    sheet = xlsx()
    downloadThreads = []
    #多线程查询
    for i in range(0, 5000, 10):
        downloadThread = threading.Thread(target=chaxun, args=(i, i + 10))#chaxun里面有for循环，args传输数据需等于步长值
        downloadThreads.append(downloadThread)
        downloadThread.start()
    # Wait for all threads to end.
    for downloadThread in downloadThreads:
        downloadThread.join()
    print('线程结束.')
    print(len(listNone))
    print(len(listadd))
    writeExcel()
    z = input('按回车键退出...')

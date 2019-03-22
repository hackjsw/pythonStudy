# coding=utf-8

import requests
import xlrd,openpyxl
import urllib.request
from bs4 import BeautifulSoup

def searchCookies():
    textPage = urllib.request.urlopen(
        "https://www.github.com/hackjsw/pythonStudy/blob/master/CookBook_and_code-master/hnjzCookie.txt")
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
        #print(result)
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
    saveCookies = searchCookies()
    chaxun()
    writeExcel()

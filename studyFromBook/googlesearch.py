#! python3
import sys,webbrowser,bs4,requests
print('input keywords: ', end='')
searchbd = input()
if len(searchbd)>1:
    print('Search...')
    res=requests.get('http://www.baidu.com/s?wd='+''.join(searchbd))
 
    #change the coding 
    res.encoding='utf-8'                     
 
    #check 
    res.raise_for_status()
 
    #Retrieve top search result links
    soup=bs4.BeautifulSoup(res.text,'lxml')
 
    #Open a browser tab for each result
    linkElems=soup.select('div.result h3.t> a')
    numOpen=min(8,len(linkElems))
    for i in range(numOpen):
        webbrowser.open(linkElems[i].get('href'))
else:
    print('Error')
    

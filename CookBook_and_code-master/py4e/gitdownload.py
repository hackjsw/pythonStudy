import urllib
from bs4 import BeautifulSoup
textPage=urllib.urlopen("https://www.github.com/hackjsw/pythonStudy/blob/master/CookBook_and_code-master/hnjzCookie.txt")
soup = BeautifulSoup(textPage,"html.parser")
cookies = soup.select("#LC1")
newCookies = cookies[0].getText()
print(newCookies)

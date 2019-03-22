from urllib import requests

resp=requests.urlopen('http://www.baidu.com')
print(type(resp))
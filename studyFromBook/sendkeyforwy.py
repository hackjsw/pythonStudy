from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://web.hunanjz.com/')
emailElem = browser.find_element_by_id('name')
emailElem.send_keys('297490519@qq.com')
passwordElem = browser.find_element_by_id('pwd')
passwordElem.send_keys('hndiliu888888')

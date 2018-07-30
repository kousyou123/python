from selenium import webdriver

browser=webdriver.Edge()
browser.get('http://selenium-python.readthedocs.io')
browser.execute_script('window.open("https://www.baidu.com");')  #在标签页打开URL
browser.execute_script('window.open("https://www.taobao.com");')

browser.back()  #后退到前一个页面
browser.set_page_load_timeout(5)
browser.forward()  #前进到下一个页面
print(browser.name)
print(browser.title)
print(browser.current_url)
print(browser.current_window_handle)
print(browser.get_cookies())
print(type(browser))
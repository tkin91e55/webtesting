import os, time
from selenium import webdriver
cwd = os.getcwd() + '/'
driver = webdriver.Chrome(cwd + 'chromedriver')
driver.get('http://www.google.com/xhtml'); 
time.sleep(5) 
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver') 
search_box.submit() 
time.sleep(5)
driver.quit() 

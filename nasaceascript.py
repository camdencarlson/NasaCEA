import requests
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# need to install the chrome driver corresponding to your version of chrome
PATH = "C:\Program Files (x86)\chromedriver.exe"
# the webdriver for chrome is located at PATH
driver = webdriver.Chrome(PATH)
driver.get('https://cearun.grc.nasa.gov/')
print(driver.title)

typecode = driver.find_element_by_id('rocket')
typecode.click()
submit1 = driver.find_element_by_name('Submit')
submit1.click()

# pressure
pvals = [1, 3, 1]
P_low = driver.find_element_by_name('P_low').send_keys(pvals[0])
P_hi = driver.find_element_by_name('P_hi').send_keys(pvals[1])
intervals = driver.find_element_by_name('P_int').send_keys(pvals[2])
aac = driver.find_element_by_name('.submit').click()  # accept and continue

# fuel
aac = driver.find_element_by_name('.submit').click()

# oxidizer
o2 = driver.find_element_by_name('oxchoice').click()
aac = driver.find_element_by_name('.submit').click()

# ratio
aac = driver.find_element_by_name('.submit').click()

# exit conditions
aac = driver.find_element_by_name('.submit').click()


# final
submitfinal = driver.find_element_by_name('.submit').click()

# extract data
output = driver.find_element_by_class_name('outputContent')
with open('output.txt', 'w') as output:
    output.write(output.text)


time.sleep(5)
print('finished')


driver.close()
driver.quit()
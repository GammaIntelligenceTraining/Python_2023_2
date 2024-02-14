from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'http://www.github.com'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.switch_to.new_window('tab')
driver.get('http://gammatest.net')
driver.switch_to.new_window('tab')
driver.get('http://google.com')

for win in driver.window_handles:
    driver.switch_to.window(win)
    driver.save_screenshot(f'{win}.png')


time.sleep(5)
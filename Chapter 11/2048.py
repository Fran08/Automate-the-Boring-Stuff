#! python3
# 2048.py - Plays the 2048 game automatically.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

html_elem = browser.find_element_by_tag_name('html')
retry_elem = browser.find_element_by_class_name('retry-button')

while True:
    
    i = random.randint(1,4)
    
    if i is 1:
        html_elem.send_keys(Keys.UP)

    elif i is 2:
        html_elem.send_keys(Keys.DOWN)

    elif i is 3:
        html_elem.send_keys(Keys.LEFT)

    elif i is 4:
        html_elem.send_keys(Keys.RIGHT)

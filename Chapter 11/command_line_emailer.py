#! python3
# command_line_emailer.py - Takes an email address, subject, and string of text on command
# line and then logs into email account and sends email of the string to address

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, time

recipient = sys.argv[1]
subject = sys.argv[2]
message = ' '.join(sys.argv[3:])

browser = webdriver.Firefox()
browser.get('https://mail.google.com')
email_elem = browser.find_element_by_id('identifierId')
email_elem.send_keys('frances.sun.python@gmail.com')
next_elem = browser.find_element_by_id('identifierNext').click()
time.sleep(3)
password_elem = browser.find_element_by_name('password')
password_elem.send_keys('Python123')
submit_elem = browser.find_element_by_id('passwordNext').click()
time.sleep(7)

compose_elem = browser.find_element_by_class_name('z0').click()
time.sleep(3)

to_elem = browser.find_element_by_xpath('//textarea[@aria-label="To"]')
to_elem.send_keys(sys.argv[1])
time.sleep(2)

subject_elem = browser.find_element_by_name('subjectbox')
subject_elem.send_keys(subject)
time.sleep(3)

text_elem = browser.find_element_by_xpath('//div[@aria-label="Message Body"]')
text_elem.send_keys(message)
time.sleep(5)

browser.find_element_by_xpath('//div[@aria-label="Send ‪(Ctrl-Enter)‬"]').click()

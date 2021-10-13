# Python program to demonstrate
# Webdriver For Firefox
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://mbasic.facebook.com")

# Firefox
driver = webdriver.Firefox()
# Google Chrome
driver = webdriver.Chrome()
# Python program Continued
# Webdriver For Firefox
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://mbasic.facebook.com")
html = driver.page_source # Getting Source of Current URL / Web-Page Loaded
print(html)
# End

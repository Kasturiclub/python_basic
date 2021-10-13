# Python program to demonstrate Facebook Login
from selenium import webdriver
  
driver = webdriver.Firefox()  
driver.get("https://mbasic.facebook.com")  
# Creating a Reference of Form For Finding Email and Password
form = driver.find_element_by_xpath("//form[@id ='login_form']")
email = form.find_element_by_name("email") 
password = form.find_element_by_name("pass")
email.send_keys("kasturip10@gmail.com")
password.send_keys("Your Facebook Password") 
submit_button = driver.find_element_by_xpath("//input[@type ='submit']")
submit_button.click() 
# Error Password in Output
# Because i had not used my real password here
# End
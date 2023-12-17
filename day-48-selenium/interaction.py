# # 005 Challenge Use Selenium in a Blank Project & Scrape a Different Piece of Data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# # 006 How to Automate Filling Out Forms and Clicking Buttons with Selenium
# article_count.click()

# english = driver.find_element(By.LINK_TEXT, "English")
# english.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# driver.get("http://secure-retreat-92358.herokuapp.com/")
# fName = driver.find_element(By.NAME, "fName")
# fName.send_keys("Al")
# lName = driver.find_element(By.NAME, "lName")
# lName.send_keys("Qahraman")
# email = driver.find_element(By.NAME, "email")
# email.send_keys("al.qahraman@gmail.com")

# button = driver.find_element(By.CSS_SELECTOR, "form button")
# button.click()



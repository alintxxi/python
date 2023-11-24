# # 001 Day 48 Goals what you will make by the end of the day
# # 002 How to Install & Set Up Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_driver_path = "C:/Users/Home Sweet Home/Desktop/Development/chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.python.org/")
# price = driver.find_element("id", "priceblock_ourprice")
# print(price.text)

# # 003 How to Find and Select Elements on a Website with Selenium
# search_bar = driver.find_element("name", "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close()
driver.quit()

from selenium import webdriver

# chrome_driver_path = "C:/Users/Home Sweet Home/Desktop/Development/chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.amazon.com")

driver.quit()
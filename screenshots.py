import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("C:/Users/tonya/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.tutorialsfreak.com/")
time.sleep(2)
# driver.save_screenshot("C:/Users/tonya/PycharmProjects/web_scraping/full_page.png")
driver.find_element(By.XPATH, """/html/body/div/div/div/section[1]/div/div[1]/div/div/div/div[3]/img""").save_screenshot("C:/Users/tonya/PycharmProjects/web_scraping/background.png")

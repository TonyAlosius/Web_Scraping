import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("C:/Users/tonya/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
search = driver.find_element(By.XPATH, """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
search.send_keys("tonyalosius.tech")
# driver.find_element(By.XPATH, """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]""")
time.sleep(2)
search.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH, """/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
time.sleep(2)
driver.find_element(By.XPATH, """/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a""").click()
time.sleep(2)
driver.save_screenshot("C:/Users/tonya/PycharmProjects/web_scraping/full_page.png")
time.sleep(100)




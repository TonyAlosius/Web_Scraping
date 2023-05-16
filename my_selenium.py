from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# s = Service("C:/Users/tonya/Downloads/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.get("https://www.wscubetech.com/")
# driver.find_element(By.XPATH, """/html/body/section[1]/div/div/div[2]/img""")
# driver.find_element_by_xpath("""/html/body/section[1]/div/div/div[1]/div/div/a""")
# # Add a delay to keep the browser open for a certain period (e.g., 5 seconds)
# time.sleep(1000)



# s = Service("C:/Users/tonya/Downloads/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.get("https://www.tutorialsfreak.com/")
# driver.find_element(By.XPATH, "/html/body/div/div/div/section[1]/div/div[1]/div/div/div/div[2]/button").click()
# # Add a delay to keep the browser open for a certain period (e.g., 5 seconds)
# time.sleep(1000)

# s = Service("C:/Users/tonya/Downloads/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.get("https://www.google.com/")
# time.sleep(1)
# search = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
# search.send_keys("tonyalosius.tech")
# time.sleep(1)
# search.send_keys(Keys.ENTER)
# time.sleep(1000)


s = Service("C:/Users/tonya/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.tutorialsfreak.com/")
driver.find_element(By.XPATH, "/html/body/div/div/div/section[1]/div/div[1]/div/div/div/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/header/nav/div/div[1]/button").click()
time.sleep(1)
ph_no = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div[2]/div[3]/form/div/input")
ph_no.send_keys("8220552122")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div[2]/div[3]/form/button").click()
time.sleep(100)

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/tonya/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/search?q=pandas&sxsrf=APwXEdd6-Yvr2L2Jtp-bs2MkfRmehkRQXQ:1684233300050&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjDx8X80fn-AhXDXGwGHXvdBPUQ_AUoAXoECAEQAw&biw=1536&bih=656&dpr=1.25")
height = driver.execute_script("return document.body.scrollHeight")
print(height)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

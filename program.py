from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

s = Service("D:/PROGRAMMING/chat bot/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://instagram.com")
time.sleep(3)
# username
driver.find_element(By.NAME, "username").send_keys("username")
# pass
driver.find_element(By.NAME, "password").send_keys("password")
# login btn
driver.find_element(By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30").click()
# search btn
searchbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.CSS_SELECTOR,
            ".x1n2onr6.x6s0dn4.x78zum5",
        )
    )
)
searchbox.click()
print("hello")

# idname
driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input",
).send_keys("username")

while True:
    pass


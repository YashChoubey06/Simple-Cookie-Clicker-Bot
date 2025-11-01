from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value = True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
english_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='English']")))
english_button.click()

# consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Got it!']")))
# consent_button.click()
#
# # 3. Wait for and click the "x" on the "Back up your save!" pop-up
# save_popup_close = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/a[1]')))
# save_popup_close.click()

cookie = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bigCookie"]')))
while True:
    driver.execute_script("arguments[0].click();", cookie)

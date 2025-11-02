from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time
from datetime import datetime

def buy_most_expensive():
    products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    product_prices = []

    for product in products:
        price_el = product.find_element(By.CSS_SELECTOR, ".price")
        text = price_el.text.replace(",", "").strip()
        if text.isdigit():
            product_prices.append((int(text), product))

    if product_prices:
        _, richest_product = max(product_prices, key=lambda x: x[0])
        driver.execute_script("arguments[0].click();", richest_product)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value = True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
english_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='English']")))
english_button.click()

wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))
last_buy_time = time.time()
start_time = time.time()


while True:
    try:
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()

        upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
        for upgrade in upgrades:
            driver.execute_script("arguments[0].click();", upgrade)

        if time.time() - last_buy_time >= 5:
            buy_most_expensive()
            last_buy_time = time.time()

        if time.time() - start_time >= 300:
            break

    except StaleElementReferenceException:

        continue

cookies_per_second = driver.find_element(By.ID, "cookiesPerSecond").text
print("Cookies per second after 5 mins:", cookies_per_second)
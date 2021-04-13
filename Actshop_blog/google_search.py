import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

bot = webdriver.Chrome("C:\\chromedriver\\chromedriver89.exe")
print("Google loaded Successfully")
bot.get("https://www.google.com/")
print("Searching aniket happiness blog")
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))).send_keys("act shop app aniket salve")
bot.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
print("clicking in aniket blog")
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="https://www.aniketsalve.com"]'))).click()
print("Happiness blog opened")
time.sleep(5)
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="How much we can earn from finance ?"]'))).click()
print("Reading blog")
time.sleep(5)
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="And here is my act shop wallet –"]'))).click()
print("Reading blog")
# Scroll down to bottom
print("Scolled down")
bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
bot.quit()
print("exit chrome")


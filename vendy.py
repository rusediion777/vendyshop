from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")

driver = webdriver.Chrome()

ids = ['606175803', '606073540', '606176079']

for id_player in ids:

    driver.get("https://wendy-shop.nexters.com/")
    time.sleep(10)
    try:
        cookes_close = driver.find_element(By.CLASS_NAME, 'cookies_popup__close_icon').click()
    except:
        time.sleep(5)

    all_html = driver.find_element(By.TAG_NAME, "html")

    for i in range (70):
        all_html.send_keys(Keys.DOWN)
    time.sleep(3)

    give_me = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/div[2]/div[2]/div[2]/div/div[5]/div/div[5]/button[1]').click()
    time.sleep(3)

    your_id = driver.find_element(By.XPATH, '//*[@id="yourId"]')
    your_id.clear()
    your_id.send_keys(id_player)
    time.sleep(5)
    give_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[7]/div[1]/button[1]').click()


    time.sleep(10)

driver.close()
driver.quit()
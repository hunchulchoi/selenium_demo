import time
import urllib.request
from io import BytesIO
from tkinter import Image

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")
assert "Google 이미지" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("나희도")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

images = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd')

for i, image in enumerate(images):
    try:
        # img = image.find_element(By.CSS_SELECTOR, '.rg_i.Q4LuWd')
        print(i, image.tag_name, image.text)
        image.click()
        time.sleep(2)
        img_url = driver.find_element(By.CSS_SELECTOR, '.n3VNCb.KAlRDb').get_attribute('src')
        print(i, img_url)
        urllib.request.urlretrieve(img_url, f'./images/{i}.jpg')
    except Exception as err:
        print('에러', img_url, err)

# driver.close()
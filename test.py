from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service("/Users/c5353574/Downloads/chromedriver"))


driver.get('https://www.youtube.com')
driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys('חדר מדרגות')
driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon').click()

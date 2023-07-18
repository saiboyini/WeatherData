from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

chromedriver_path = 'C:\webdrivers\chromedriver'
driver = webdriver.Chrome('') 

driver.get("https://www.visualcrossing.com")
time.sleep(1)

cookies = driver.find_element(by=By.XPATH, value= "/html/body/main/span/div/div[4]/div/div/div[2]/div[2]/button[1]")
cookies.click()
time.sleep(2)

weather_button=driver.find_element(by=By.CSS_SELECTOR, value="#navbarNav > ul > li:nth-child(1) > a")
weather_button.click()
time.sleep(4)

weather_search_button = driver.find_element(by=By.XPATH, value= "/html/body/main/section[1]/div/div[2]/div[2]/form/div[1]/input")
weather_search_button.send_keys("Hyderabad")
weather_search_button.send_keys(Keys.RETURN)
time.sleep(4)

checking_page = driver.find_element(by=By.XPATH, value='/html/body/main/section[1]/h1')
assert checking_page.text == 'Historical weather data for Hyderabad'

driver.execute_script("window.scrollBy(0, 300)")
time.sleep(4)

driver.execute_script("window.scrollBy(300, 600)")
time.sleep(4)

driver.execute_script("window.scrollBy(600, 700)")
time.sleep(4)

driver.execute_script("window.scrollBy(600, 750)")
time.sleep(21)
# weather_search_button_click = driver.find_element(by=By.XPATH, value= "//*[@id="wxdataform"]/div[2]/button")
# weather_search_button.click()
# time.sleep(40)



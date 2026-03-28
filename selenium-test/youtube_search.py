from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com")
time.sleep(2)
driver.maximize_window()

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("open source software")
search_box.send_keys(Keys.RETURN)

time.sleep(8)
driver.quit()
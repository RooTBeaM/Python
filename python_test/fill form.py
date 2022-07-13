
from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = 'C:\Program Files (x86)\chromedriver.exe'
# web = webdriver.Chrome(path)
# web.get('https://youtube.com')
# time.sleep(5)
# search_box = web.find_element(By.XPATH,'//input[@id="search"]')
# search_box.send_keys('web automation python')
# search_button = web.find_element(By.XPATH,'//*[@id="search-icon-legacy"]')
# print(web.title)
# search_button.click()


# time.sleep(5)
# web.close()
# print("we done now!!!")

# ////////////////////////////////////////////////////////////////////////////////////////////
# driver = webdriver.Chrome(path)
# driver.delete_all_cookies()
# driver.set_page_load_timeout(40)
# driver.implicitly_wait(10)
# driver.get("https://login.yahoo.com/account/create")
# driver.find_element(By.XPATH, "//input[@id='usernamereg-firstName']").send_keys("aaaaYour-Name")
# driver.find_element(By.XPATH, "//input[@id='usernamereg-lastName']").send_keys("bbbYour-Last_name")
# driver.find_element(By.XPATH, "//input[@id='usernamereg-userId']").send_keys("email@yahoo.com")
# driver.find_element(By.XPATH, "//input[@id='usernamereg-password']").send_keys("123456789")
# driver.find_element(By.XPATH, "//input[@id='usernamereg-birthYear']").send_keys("1999")
# time.sleep(3)
# driver.find_element(By.XPATH, "//button[@id='tpa-google-button']").click()
# //////////////////////////////////////////////////////////////////////////////++

driver = webdriver.Chrome(path)
driver.get("https://accounts.google.com/signup")

driver.find_element(By.PARTIAL_LINK_TEXT, "ช่วยเหลือ").click()

#prints parent window title
print("Parent window title: " + driver.title)

#get current window handle
p = driver.current_window_handle
time.sleep(3)
#get first child window
chwd = driver.window_handles

driver.switch_to.window(chwd[0])


time.sleep(2)
print("Child window title: " + driver.title)

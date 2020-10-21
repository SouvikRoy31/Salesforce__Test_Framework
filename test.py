import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import functionLibrary as Fl
from xml.etree.ElementTree import parse


env = parse('environment.xml')
for item in env.iterfind('sandbox_oct'):
    user_id = item.findtext('uname')
    password = item.findtext('password')
    url = item.findtext('url')
    browser = item.findtext('browser')
Fl.close_browser(browser)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(5)
driver.find_element_by_id("username").send_keys(user_id)  # username
# time.sleep(5)
driver.find_element_by_id("password").send_keys(password)  # password
# time.sleep(5)
driver.find_element_by_id("Login").click()  # login btn press
# page_sync_class("slds-global-header__logo", 10)

xpathCount = driver.find_elements_by_xpath('//*[@data-aura-class="oneConsoleTabItem"]')
print(len(xpathCount))

time.sleep(5)
driver.find_element_by_class_name("slds-context-bar__icon-action").click()
time.sleep(5)
Fl.search_and_click(driver, '//*[@placeholder="Search apps and items..."]', 'Leads')

# driver.find_element_by_xpath('//*[@placeholder="Search apps and items..."]').send_keys('Leads')
# time.sleep(5)
# driver.find_element_by_xpath('//*[@placeholder="Search apps and items..."]').send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_link_text("New").click()
time.sleep(15)


import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def close_browser(c_browser):
    os.system('taskkill /F /Fi "imagename eq {}"'.format(c_browser))





def search_and_click(driver, xpath, value):
    driver.find_element_by_xpath(xpath).send_keys(value)
    time.sleep(5)
    driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)


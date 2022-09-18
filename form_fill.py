from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



def start_au(login, password):
    url = "https://ya.ru/"
    driver = webdriver.Firefox()

    driver.get(url)

    element_login = driver.find_element(by=By.NAME, value="text")
    #element_password = driver.find_element(by=By.NAME, value="text")

    element_login.click()
    element_login.send_keys(login)

    """element_password.click()
    element_password.send_keys(password)"""
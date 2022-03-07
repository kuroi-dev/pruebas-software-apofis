from lib2to3.pgen2 import driver
import timeit
import time
import math
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



driver = webdriver.Chrome('./chromedriver')

inicio = time.time()

timeout = 30


driver.get('https://www.jumbo.cl/')
driver.set_window_size(1400, 1200)



def login():
    try:
        user = driver.find_element_by_xpath('//*[@id="root"]/div/header/div[3]/div/div[2]/div[1]/button[2]')
        WebDriverWait(driver, timeout).until(user)
    except TimeoutException:
        print ("Timed out waiting for page to load")
login()


fin = time.time()
print(fin-inicio)
driver.close()
quit()



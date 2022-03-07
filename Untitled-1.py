
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
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome('./chromedriver')

inicio = time.time()

timeout = 6


driver.get('https://www.lider.cl/')
driver.set_window_size(1400, 1000)



def login():
    try:
        user = EC.presence_of_element_located(By.XPATH,'//*[@id="prehomegr_card_icono_supermercado"]')
        WebDriverWait(driver, timeout).until(user)
    except TimeoutException:
        print ("Timed out waiting for page to load")



fin = time.time()
print(fin-inicio)
driver.close()
quit()



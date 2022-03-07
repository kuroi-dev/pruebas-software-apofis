import timeit
import time
import math
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome('./chromedriver')

inicio = time.time()

driver.get("https://lider.cl/")
try:
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "prehomegr_card_icono_supermercado")))
	driver.get("https://www.lider.cl/supermercado/")
	element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bannerCarousel")))
    
finally:
	print("Timed out waiting for page to load")

driver.quit()
fin = time.time()
print(fin-inicio)
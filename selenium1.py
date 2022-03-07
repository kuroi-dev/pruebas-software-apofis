import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#ABRIR NAVEGADOR_____________________________________________________________________________

browser = webdriver.Chrome('./chromedriver')



#INGRESAR URL________________________________________________________________________________

browser.get('https://docs.google.com/forms/d/e/1FAIpQLScTiUASURXnFVuyoIPhD_cGFwSLs61glnvJ7Sp400NxQQmfhg/viewform')

sleep(random.uniform(1.0,2.0))



#INGRESAR MAIL_______________________________________________________________________________

mail = browser.find_element_by_xpath('//input[@jsname="YPqjbf"]')

sleep(random.uniform(1.0,2.0))

mail.click()

sleep(random.uniform(1.0,2.0))

mail.send_keys('driquelme@atentus.com')

sleep(random.uniform(1.0,2.0))



#INGRESAR PERSONA____________________________________________________________________________

selector1 = browser.find_element_by_xpath('//div[@aria-labelledby="i5"]')

sleep(random.uniform(1.0,2.0))

selector1.click()

sleep(random.uniform(1.0,2.0))

yo = browser.find_element_by_tag_name('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div > div.freebirdFormviewerComponentsQuestionSelectRoot > div > div:nth-child(2) > div:nth-child(15)')

sleep(random.uniform(1.0,2.0))

yo.click()

sleep(random.uniform(1.0,2.0))



#INGRESAR DIA________________________________________________________________________________

selector2 = browser.find_element_by_xpath('//div[@aria-labelledby="i9"]')

sleep(random.uniform(1.0,2.0))

selector2.click()

sleep(random.uniform(1.0,2.0))

dia = browser.find_element_by_tag_name('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionSelectRoot > div > div:nth-child(2) > div:nth-child(3)')

sleep(random.uniform(1.0,2.0))

dia.click()

sleep(random.uniform(1.0,2.0))



#INGRESAR FECHA______________________________________________________________________________

selector3 = browser.find_element_by_xpath('//input[@aria-labelledby="i17"]')

sleep(random.uniform(1.0,2.0))

selector3.send_keys('16022021')



#INGRESAR HORA________________________________________________________________________________

selector3 = browser.find_element_by_xpath('//input[@type="number"]')

sleep(random.uniform(1.0,2.0))

selector3.send_keys('08',Keys.TAB,'00')
sleep(random.uniform(1.0,2.0))



#ACEPTAR______________________________________________________________________________________

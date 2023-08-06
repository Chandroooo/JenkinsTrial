"This code goes to google.com and enters keyword 'Guvi' and enters it..  and will click on the first link "

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from time import sleep

class GoogleSearch:

    def __init__(self):
        self.url = "https://www.google.com/"
        self.driver = webdriver.Chrome()
        self.keyword = "Guvi"
        self.keyword_locator_name_tag = "q"
        self.SearchButton = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]"
        self.FirstLink = "//h3[contains(text(),'GUVI')]"

    def browse(self):
        self.driver.get(self.url)
        print(self.driver.title)
        self.driver.maximize_window()
        time.sleep(3)

    def input_credentials(self):
        keyword_webelement = self.driver.find_element(By.NAME, self.keyword_locator_name_tag)
        keyword_webelement.send_keys(self.keyword)
        time.sleep(3)

        keyword_webelement.send_keys(Keys.ENTER)

    def Guvi_FirstLink(self):
        FirstLink_webelement = self.driver.find_element(By.XPATH, self.FirstLink)
        FirstLink_webelement.click()
        time.sleep(3)



        # SearchButton_webelement = self.driver.find_element(By.XPATH, self.SearchButton)
        # SearchButton_webelement.click()



obj = GoogleSearch()
obj.browse()
obj.input_credentials()
obj.Guvi_FirstLink()
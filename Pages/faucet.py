from BaseClass.base import BaseClass
from Configurations.config import TestConfig
import time
from selenium.webdriver.common.by import By


class faucetPageClass(BaseClass):

    explorer=(By.XPATH,'//span[text()="Explorer"]')
    search_bar=(By.XPATH ,'//input[@name="q"]')
    hekla_button_switch_to_holesky=(By.XPATH ,'//label[text()="You are currently on"]//following-sibling::button')
    holesky=(By.XPATH ,'//span[text()="Holesky"]')
    mint=(By.XPATH ,'//span[text()="Mint"]')


   
    
    def __init__(self , driver):
        super().__init__(driver)


    def click_on_explorer(self):
        self.click_on_element(self.explorer)

    def click_on_Mint(self):
        self.click_on_element(self.mint)



    def click_on_searchBox(self):
        self.click_on_element(self.search_bar)
        self.input_element(TestConfig.meta_mask_address)

    
    def click_on_hekla_button_switch_to_holesky(self):
        self.click_on_element(self.hekla_button_switch_to_holesky)
        time.sleep(5)
        self.click_on_element(self.holesky)

   
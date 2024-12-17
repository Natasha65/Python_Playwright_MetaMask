from Configurations.config import TestConfig
from selenium.webdriver.support import wait , expected_conditions as EC
import datetime
from selenium.webdriver.common.by import By
import os
from utilities.wait import Waits
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException, \
    NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, \
    InvalidSelectorException  , ElementClickInterceptedException as EX


logs=TestConfig.get_logs

class BaseClass:
    

    def __init__(self , driver):
        self.driver=driver
        self.wait=Waits(driver)


    def wait_time(self , wait_time):
        wait.WebDriverWait(self , wait_time)


    def click_on_element(self, ByLocator):
        try:
            self.wait.waitForElementVisibility1(ByLocator , 10)
            element=self.wait.waitForElementToBeClickable(ByLocator , 10)
            element.click()
        except EX as e:
            print("Exception! Can't click on the element")


    def click_element(self, ByLocator):
        try:
            element=self.wait.waitForElementToBeClickable(ByLocator , TestConfig.IMPLICIT_WAIT)
            element.click()
        except EX as e:
            print("Element is not clicked")

    

    def get_element_by_text(self ,ByLocator):
        try:
            element=self.driver.find_element(By.XPATH , "(//div[contains(@data-testid,'primary-currency')]/span)[1]")
            return element.text
        
        except:
            print("Element is not clicked ")


    def is_element_displaying(self , ByLocator):
        try:
            self.wait.waitForElementVisibility1(ByLocator , TestConfig.IMPLICIT_WAIT )
            element=self.wait.waitForElementToBeClickable(ByLocator , TestConfig.IMPLICIT_WAIT )
            return element.is_displayed()
        
        except:
            return False
    

    def take_screenshot(self):
        current_date_time = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
        screenshot_path = os.path.join(os.path.abspath('meta-mask/Reports/Screenshots'),
                                       f"Failed_Screenshots_{current_date_time}.png")
        self.driver.save_screenshot(screenshot_path)

    
    def input_element(self, ByLocator, Text):
        try:
            element=self.wait.waitForElementVisibility1(ByLocator , TestConfig.IMPLICIT_WAIT) 
            element.send_keys(Text)
        except EX as e:
            print(f"Exception! Can't click on the element >>> {e}")

    
    def input_element1(self, ByLocator, Text):
        try:
            element=self.wait.waitForElementToBeClickable(ByLocator , TestConfig.IMPLICIT_WAIT) 
            # element.click()
            element.send_keys(Text)
        except EX as e:
            print(f"Exception! Can't click on the element >>> {e}")






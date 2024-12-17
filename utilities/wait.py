from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Waits:
    def __init__(self, driver):
        self.driver = driver

    def wait1s(self):
        self._wait(1)

    def wait2s(self):
        self._wait(2)

    def wait3s(self):
        self._wait(3)

    def wait4s(self):
        self._wait(4)

    def wait5s(self):
        self._wait(5)

    def wait6s(self):
        self._wait(6)

    def waitTime(self, time):
        self._wait(time)

    def waitForElementToBeClickable(self, element, timeOutInSeconds):
        wait = WebDriverWait(self.driver, timeOutInSeconds)
        return wait.until(EC.element_to_be_clickable(element))

    def waitForElementVisibility1(self, element, timeoutInSeconds):
        wait = WebDriverWait(self.driver, timeoutInSeconds)
        return wait.until(EC.visibility_of_element_located(element))
        
    

        

    def waitfor10sec(self):
        self._wait(10)

    def waitfor10mints(self):
        self._wait(600)

    def waitfor3sec(self):
        self._wait(3)

    def waitfor5sec(self):
        self._wait(5)

    def waitfor1sec(self):
        self._wait(1)

    def Waitfor10mints(self):
        self._wait(600)

    def _wait(self, seconds):
        try:
            self.driver.implicitly_wait(seconds)
        except Exception as e:
            print(e)

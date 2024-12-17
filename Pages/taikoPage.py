from BaseClass.base import BaseClass
from selenium.webdriver.common.by import By
from pyshadow.main import Shadow


class taikoPageClass(BaseClass):

    ConnectButton=(By.XPATH,'/html/body/div/div[1]/div[1]/header/div/button/div')
    I_understand_button=(By.XPATH ,'//button[text()="I understand"]')
    hekla=(By.XPATH ,'/html/body/div/dialog[1]/div/ul/li[2]')
    holesky=(By.XPATH ,'/html/body/div/dialog[1]/div/ul/li[1]/div')
    # eth=(By.XPATH ,'//span[text()="2.7996 ETH"]')
    eth=(By.XPATH , '//img[@class="w-[24px]"]//following-sibling::span')
    amount=(By.XPATH , '//input[@type="number"]')
    Continue=(By.XPATH , '//span[text()="Continue"]')
    Bridge=(By.XPATH , '//span[text()="Bridge"]')
    successMessage=(By.XPATH , '//h1[text()="Transaction completed"]')
    
    def __init__(self , driver):
        super().__init__(driver)


    def click_on_connectWalletButton(self):
        self.click_on_element(self.ConnectButton)
    

    def click_on_ContinueButton(self):
        self.click_on_element(self.Continue)

    
    def isTransactionCompleteMessageDisplaying(self):
        self.is_element_displaying(self.successMessage)



    def click_on_IUnderstand(self):
        self.click_on_element(self.I_understand_button)


    
    def click_on_Bridge(self):
        self.click_on_element(self.Bridge)

    
    def click_on_hekla(self):
        self.click_on_element(self.hekla)

    
    def click_on_holesky(self):
        self.click_on_element(self.holesky)
    

    def click_on_ETH(self):
        self.click_on_element(self.eth)

    
    def enterAmount(self , amount):
        self.click_on_element(self.amount)
        self.input_element(self.amount , amount)



    

    def click_on_Holesky(self):
        shadow=Shadow(self.driver)
        element=shadow.find_element("wui-list-item")
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        button_within_shadow = shadow_root.find_element(By.CSS_SELECTOR ,"button")
        button_within_shadow.click()

    
    def click_on_Hekla_ShadowElement(self):
        shadow=Shadow(self.driver)
        element=shadow.find_element("wui-card-select[name='Hekla']")
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        button_within_shadow = shadow_root.find_element(By.CSS_SELECTOR ,"button")
        button_within_shadow.click()
    




    
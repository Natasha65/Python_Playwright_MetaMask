
from BaseClass.base import BaseClass
from selenium.webdriver.common.by import By
from pyshadow.main import Shadow
from Configurations.config import TestConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class metaMaskPageClass(BaseClass):

    NextButton=(By.XPATH,'//button[text()="Next"]')
    MetaMaskButton=(By.XPATH, '/html/body/w3m-modal//wui-flex/wui-card/w3m-router//div/w3m-connect-view//wui-flex/wui-list-wallet[3]//button/wui-text')
    Password=(By.XPATH, '//input[@type="password"]')
    unLock=(By.XPATH,'//button[text()="Unlock"]')
    checkbox=(By.XPATH,'//input[@id="onboarding__terms-checkbox"]')
    checkbox1=(By.XPATH,'//input[@type="checkbox"]')
    existing_wallet_button=(By.XPATH,'//button[text()="Import an existing wallet"]')
    i_agree_button=(By.XPATH,'//button[text()="I agree"]')
    confirm_secret_key=(By.XPATH , '//button[text()="Confirm Secret Recovery Phrase"]')
    ConfirmPassword=(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input')
    importWalletButton=(By.XPATH ,'//button[text()="Import my wallet"]')
    GotIt_Button=(By.XPATH ,'//button[text()="Got it"]')
    Next_Button=(By.XPATH ,'//button[text()="Next"]')
    Done_Button=(By.XPATH ,'//button[text()="Done"]')
    NotRightNow_Button=(By.XPATH ,'//button[text()="Not right now"]')
    connect=(By.XPATH,'//button[text()="Connect"]')
    approve=(By.XPATH,'//button[text()="Approve"]')
    createNewWallet=(By.XPATH , '//button[text()="Create a new wallet"]')
    switch_network=(By.XPATH,'//button[text()="Switch network"]')
    secureMyWallet=(By.XPATH ,'//button[text()="Secure my wallet (recommended)"]')
    reveal=(By.XPATH , '//button[text()="Reveal Secret Recovery Phrase"]')
    copy_clipboard=(By.XPATH , '//a[text()="Copy to clipboard"]')
    account=(By.XPATH , '//span[text()="Account 1"]')
    addAccount=(By.XPATH ,'//button[text()="Add account or hardware wallet"]')
    importAccount=(By.XPATH , '//button[text()="Import account"]')
    importButton=(By.XPATH ,'//button[text()="Import"]')
    confirm=(By.XPATH ,'//button[text()="Confirm"]')
    seePortolio = (By.XPATH, '//button[text()="See Portfolio"]')
    sendButton=(By.XPATH ,'//p[text()="Send"]')
    send_to_Account1=(By.XPATH ,'//p[text()="Account 1"]')
    amountToSend=(By.XPATH ,'//input[@data-testid="currency-input"]')
    transactionConfirmMessage=(By.XPATH, '//div[text()="Confirmed"]')
    balance=(By.XPATH ,"(//div[contains(@data-testid,'primary-currency')]/span)[1]")
    


    def __init__(self , driver):
        
        super().__init__(driver)

    def click_on_MetaMask(self):
        shadow=Shadow(self.driver)
        element=shadow.find_element("wui-list-wallet[name='MetaMask']")
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        button_within_shadow = WebDriverWait(shadow_root, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
        )
        # button_within_shadow = shadow_root.find_element(By.CSS_SELECTOR ,"button")
        button_within_shadow.click()

    def click_on_nextButton(self):
        self.click_on_element(self.NextButton)

    def click_on_Confirm(self):
        self.click_on_element(self.confirm)

    
    
    def click_on_SeePortfolio(self):
        self.click_on_element(self.seePortolio)

    
    def getBalance(self):
        self.get_element_by_text(self.balance)

    
    def click_on_send(self):
        self.click_on_element(self.sendButton)
    

    def click_on_AmountToSend(self):
        self.click_on_element(self.amountToSend)

    
    def enter_AmountToSend(self ):
        self.input_element1(self.amountToSend , TestConfig.AmountToSend)

    
    def click_on_existing_wallet(self):
        self.click_on_element(self.existing_wallet_button)

    
    def click_on_connect(self):
        self.click_on_element(self.connect)


    def click_on_password(self):
        self.click_on_element(self.Password)


    def click_on_confirm_phrase(self):
        self.click_on_element(self.confirm_secret_key)
    

    def click_on_import_wallet(self):
        self.click_on_element(self.importWalletButton)

    
    def click_on_secure_myWallet(self):
        self.click_on_element(self.secureMyWallet)

    
    def click_on_send_ToAccount1(self):
        self.click_on_element(self.send_to_Account1)

    
    def click_on_copyClipboard(self):
        self.click_on_element(self.copy_clipboard)

    
    def click_on_Account(self):
        time.sleep(5)
        self.click_on_element(self.account)
    
    def enter_phrase(self):
            phrase="raw reopen gown harvest right arm potato equip act deliver flush mesh"
            words=phrase.split()
            for i in range(0, 12):
                 xpath=f"//input[@id='import-srp__srp-word-{i}']"
                 print(xpath)
                 element=self.driver.find_element(By.XPATH , xpath)
                 element.send_keys(words[i])

    

    def enter_phrase2(self , phrase):
            words=phrase.split()
            indices_to_fill = [2, 3, 7]
            for i in indices_to_fill:
                xpath = f"//input[@data-testid='recovery-phrase-input-{i}']"
                element = self.driver.find_element(By.XPATH, xpath)
                element.send_keys(words[i])



    
    def click_on_Iagree(self):
        self.click_on_element(self.i_agree_button)



    def click_on_Import(self):
        self.click_on_element(self.importButton)


    
    def click_on_GotIt(self):
        self.click_on_element(self.GotIt_Button)


    def click_on_addAccount(self):
        self.click_on_element(self.addAccount)

    
    def click_on_PrivateKey(self):
        self.click_on_element(self.Password)

    
    def enterPrivateKey(self):
        self.input_element(self.Password , TestConfig.private_key_Parent_Wallet)


    def click_on_Reveal(self):
        self.click_on_element(self.reveal)
    

    


    def enter_password(self , password):
        self.input_element(self.Password , password)

    def enter_confirm_password(self , password):
        self.input_element(self.ConfirmPassword , password)

    def click_on_unlock(self):
        self.click_on_element(self.unLock)

    
    def click_on_createNewWallet(self):
        self.click_on_element(self.createNewWallet)


    def click_on_checkbox(self):
        self.click_on_element(self.checkbox)

    def click_on_ImportAccount(self):
        self.click_on_element(self.importAccount)


    def click_on_checkbox1(self):
        self.click_on_element(self.checkbox1)

    def click_on_Next(self):
        self.click_on_element(self.Next_Button)

    
    def isMessagePresent(self):
        self.is_element_displaying(self.Next_Button)

    
    def click_on_Done(self):
        self.click_on_element(self.Done_Button)

    
    def click_on_NotRightNow(self):
        self.click_on_element(self.NotRightNow_Button)

    
    def click_on_approve(self):
        self.click_on_element(self.approve)

    def click_on_switchNetwork(self):
        self.click_on_element(self.switch_network)

    




    
    

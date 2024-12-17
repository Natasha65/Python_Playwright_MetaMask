from BaseClass.base import BaseClass
from Configurations.config import TestConfig
from Pages.taikoPage import taikoPageClass
from Pages.metamaskPage import metaMaskPageClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import wait , expected_conditions as EC
import time
from Pages.faucet import faucetPageClass
from utilities.wait import Waits
from selenium.webdriver.common.by import By
import pyperclip

logs=TestConfig.get_logs()

        

def test_createWalletAndTransferFunds():

        driver=TestConfig.chrome_browser()
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome')
        metaMask_Page=metaMaskPageClass(driver)
        faucet_page=faucetPageClass(driver)
        taikoPage=taikoPageClass(driver)
        wait=Waits(driver)

        driver.switch_to.window(driver.window_handles[0])
        logs.info("Launch the Meta Mask to Create a Wallet")
        metaMask_Page.click_on_checkbox()

        logs.info("Click on Create New wallet")
        metaMask_Page.click_on_createNewWallet()

        logs.info("Click on I agree")
        metaMask_Page.click_on_Iagree()
        
        
        logs.info("Enter Password")
        metaMask_Page.enter_password(TestConfig.PASSWORD)

        logs.info("Enter Confirm Password")
        metaMask_Page.enter_confirm_password(TestConfig.PASSWORD)

        logs.info("Click On checkbox")
        metaMask_Page.click_on_checkbox1()

        logs.info("Click On Create a New wallet")
        metaMask_Page.click_on_createNewWallet()

        logs.info("Click On secure my wallet")
        metaMask_Page.click_on_secure_myWallet()


        logs.info("Click On Reveal")
        metaMask_Page.click_on_Reveal()

        logs.info("Click On Copy to Clipboard")
        metaMask_Page.click_on_copyClipboard()

        copied_text = pyperclip.paste()

        logs.info("Click On Next")
        metaMask_Page.click_on_Next()

        logs.info("Enter the phrase")
        metaMask_Page.enter_phrase2(copied_text)

        logs.info("Click On Confirm Phrase")
        metaMask_Page.click_on_Confirm()


        logs.info("Click On got it ")
        metaMask_Page.click_on_GotIt()

    
        logs.info("Click On Next")
        metaMask_Page.click_on_Next()

        logs.info("Click On Done")
        metaMask_Page.click_on_Done()

        logs.info("Click On Not Right Now ")
        metaMask_Page.click_on_NotRightNow()


        # switching the network 
        driver.get("https://bridge.hekla.taiko.xyz/")
        

        logs.info("Click on I Understand Button")
        taikoPage.click_on_IUnderstand()

        logs.info("Click on Connect Wallet Button")
        taikoPage.click_on_connectWalletButton()
        

        logs.info("Click on Meta Mask Button")
        time.sleep(5)
        metaMask_Page.click_on_MetaMask()

        time.sleep(5)
        driver.switch_to.new_window()
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        # driver.switch_to.window(driver.window_handles[2])


        logs.info("Click on Next button")
        time.sleep(5)
        metaMask_Page.click_on_Next()
        

        logs.info("Click on Connect button")
        metaMask_Page.click_on_connect()

        driver.switch_to.window(driver.window_handles[0])
        logs.info("Click on Holesky")
        taikoPage.click_on_holesky()

        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        logs.info("Click on Approve Button")
        time.sleep(5)
        metaMask_Page.click_on_approve()

        logs.info("Click on switch Network")
        metaMask_Page.click_on_switchNetwork()


        logs.info("Navigate to Taiko for switch the network")
        driver.get("https://bridge.hekla.taiko.xyz/")


        driver.switch_to.window(driver.window_handles[1])
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        for i in range(0 , 4):
                logs.info("Click On got it ")
                time.sleep(2)
                metaMask_Page.click_on_GotIt()
                time.sleep(5)
        
        logs.info("Click On See portfolio")
        metaMask_Page.click_on_SeePortfolio()



        driver.switch_to.window(driver.window_handles[2])
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')


        logs.info("Click On Account ")
        metaMask_Page.click_on_Account()

        logs.info("Click On Add Accounts ")
        metaMask_Page.click_on_addAccount()


        logs.info("Click On Import Account ")
        metaMask_Page.click_on_ImportAccount()


        logs.info("Click On Private Key ")
        metaMask_Page.click_on_PrivateKey()


        logs.info("Enter Private Key ")
        metaMask_Page.enterPrivateKey()


        logs.info("Click On Import")
        metaMask_Page.click_on_Import()



        time.sleep(5)
        element=driver.find_element(By.XPATH , "(//div[contains(@data-testid,'primary-currency')]/span)[1]")
        balance=element.text
        logs.info(balance)
        # balance1=float(balance)
        # amountToSend = (75 / 100) * balance1
        # logs.info(amountToSend)



        time.sleep(5)
        logs.info("Click On Send")
        metaMask_Page.click_on_send()

        driver.switch_to.new_window()
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#send')


        
        logs.info("Click On Account1")
        time.sleep(5)
        metaMask_Page.click_on_send_ToAccount1()

        time.sleep(5)
        logs.info("Enter Amount")
        metaMask_Page.enter_AmountToSend()



        logs.info("Click On Next")
        metaMask_Page.click_on_Next()

        time.sleep(5)
        logs.info("Click On Confirm")

        time.sleep(5)
        metaMask_Page.click_on_Confirm()

        time.sleep(30)
        logs.info("Transaction is succcessfull")
        metaMask_Page.isMessagePresent()
        

        driver.switch_to.new_window()
        logs.info("Navigate to Hekla Faucet")
        driver.get("https://bridge.hekla.taiko.xyz/faucet/")


        logs.info("Click On Mint")
        time.sleep(5)
        faucet_page.click_on_Mint()
        time.sleep(5)


        
        logs.info("Click On Confirm")   
        driver.switch_to.new_window()
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        time.sleep(10)
        metaMask_Page.click_on_Confirm()
        time.sleep(10)

        driver.get("https://bridge.hekla.taiko.xyz/")

        

        logs.info("Enter Amount")
        taikoPage.enterAmount(TestConfig.enterAmountToTaiko)
        

        logs.info("Click On Continue")
        taikoPage.click_on_ContinueButton()
        time.sleep(5)


        logs.info("Click On Continue")
        taikoPage.click_on_ContinueButton()


        time.sleep(5)
        logs.info("Click On Bridge")
        taikoPage.click_on_Bridge()


        time.sleep(5)
        logs.info("Click On Confirm")
        driver.switch_to.new_window()
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        time.sleep(10)
        metaMask_Page.click_on_Confirm()
        time.sleep(5)


        # driver.get("https://bridge.hekla.taiko.xyz/")
        driver.switch_to.window(driver.window_handles[6])
        logs.info("Verify the transaction successfull messages")
        time.sleep(5)
        taikoPage.isTransactionCompleteMessageDisplaying()



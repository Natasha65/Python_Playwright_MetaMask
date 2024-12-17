
import datetime
from datetime import datetime
import os
import logging
from selenium import webdriver
class TestConfig:
    BROWSER = 'chrome'
    PASSWORD='@Software666'
    URL='https://bridge.hekla.taiko.xyz/'
    IMPLICIT_WAIT=20
    meta_mask_address="0x375cc6a11b7F34970163278b01de8F741d5696eD"
    private_key_Parent_Wallet="c750b6073f2687f414130b3eb962a3626fa905d8f1d26fd2148fc9fb9573b604"
    AmountToSend=0.22188
    enterAmountToTaiko=0.02



        #The purpose of this method is to create and configure a logger for 
        #logging messages in a Python application.
        #It sets up a logger with a specific log format and saves log messages to a file

    @staticmethod
    def get_logs():
        #Retrieves the current timestamp in the format "%d_%m_%y_%H_%M_%S" (day_month_year_hour_minute_second).
        TimeStamp = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
        #This timestamp will be used to create a unique log file name.
        TimeOnly = str(datetime.now())
        LogFileName = "logs_" + f"test_{TimeStamp}.log"

        #Creates the full path to the log file by joining the absolute path of the meta-mask/Logs directory with the constructed log file name.
        LogPath = os.path.join(os.path.abspath('meta-mask/Logs'), f"{LogFileName}")
        #Initializes a logger object using the timestamp (converted to a string) as the logger name.
        Logger = logging.getLogger(TimeOnly)
        logging.basicConfig(datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
        #opening the file in  write mode to overwrite the content
        Filehandler = logging.FileHandler(LogPath, mode="w")
        Formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                    datefmt='%d/%m/%Y %I:%M:%S %p')
        Filehandler.setFormatter(Formatter)
        Logger.addHandler(Filehandler)
        Logger.setLevel(logging.INFO)
        return Logger





    def headless_chrome_browser():
        options=webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_extension(r'C:\Users\codeautomation\Desktop\metamask-automation-v2\metamask-automation\meta-mask\Extensions\MetaMask.crx')
        return webdriver.Chrome(options=options)


    

    def chrome_browser():
        options=webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach" , True)
        options.add_extension(r'C:\Users\codeautomation\Desktop\metamask-automation-v2\metamask-automation\meta-mask\Extensions\MetaMask.crx')
        return webdriver.Chrome(options=options)


    

    def chrome_parameter_browser(headless):
        options=webdriver.ChromeOptions()
        if headless:
            options=webdriver.Chrome("--headless=new")
        else:
            options.add_argument("start-maximized")
            options.add_extension(r'C:\Users\codeautomation\Desktop\metamask-automation-v2\metamask-automation\meta-mask\Extensions\MetaMask.crx')
            # options.add_argument(r'--user-data-dir=C:\Users\codea\AppData\Local\Google\Chrome\User Data')
            # options.add_argument(r'--profile-directory=Profile 3')
            options.add_experimental_option("detach" , True)
            driver=webdriver.Chrome(options)
        return driver



















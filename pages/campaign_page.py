import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class Campaign_page(BaseDriver):
    log = Utils.custlogger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    # Locators
    CAMPAIGN_MENU_FIELD = "//span[contains(@class,'mr-2') and contains(text(),'Campaigns')]"
    CLIENT_DROPDOWN = "//app-select-async[@label='name']"
    SEARCH_BOX_FIELD = "//div[@class='mat-select-search-inner mat-typography mat-datepicker-content mat-tab-header']/input"
    # SELECT_CLIENT_FIELD = "//span[normalize-space()='Breakroom']"
    SELECT_CLIENT_FIELD = "//span[@class='mat-option-text']"
    # c_drpdwn = "//span[@class='mat-select-value-text ng-tns-c41-510 ng-star-inserted'][1]"
    # srch_box = "//input[@id='mat-input-249']"

    

    def getCampaignMenuField(self):
        return self.driver.find_element(By.XPATH, self.CAMPAIGN_MENU_FIELD)

    def getClientDropdownField(self):
        return self.wait_until_element_clickable(By.XPATH, self.CLIENT_DROPDOWN)

    def getSearchBoxField(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BOX_FIELD)

    def getSelectClientField(self):
        return self.driver.find_elements(By.XPATH, self.SELECT_CLIENT_FIELD)

    def enter_Campaign_Page_Field(self):
        self.getCampaignMenuField().click()
        time.sleep(4)

    # This will select the client from client dropdown
    def enter_Client_Dropdwn_Field(self, client1):
        # var4 = self.driver.find_element(By.XPATH, self.c_drpdwn)
        time.sleep(7)
        self.getClientDropdownField().click()
        time.sleep(4)
        self.getSearchBoxField().click()
        self.getSearchBoxField().send_keys(client1)
        time.sleep(5)
        self.log.info("Selected client name " +client1)
        search_result = self.getSelectClientField()
        for result in search_result:
            if client1 in result.text:
                result.click()
                break
        self.log.info("Client selected")
        time.sleep(10)




















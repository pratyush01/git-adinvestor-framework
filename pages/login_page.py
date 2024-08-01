import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from pages.campaign_page import Campaign_page
from utilities.utils import Utils

class Login_page(BaseDriver):
    log = Utils.custlogger()
    def __init__(self, driver):
        self.driver = driver
        # self.wait = wait

    # Locators
    USER_FIELD = "username"
    PASS_FIELD = "password"
    LOGIN_BUTTON = "//span[normalize-space()='Sign in']"
    REVW_BUTTON = "//span[normalize-space()='Review Now']"
    # ACTN_RQRD = "//span[contains(text(),'Action Required: Review account budgets and rules')]"

    def getUserName(self):
        return self.driver.find_element(By.NAME, self.USER_FIELD)

    def getPasswordField(self):
        return self.driver.find_element(By.NAME, self.PASS_FIELD)

    def getLoginButtonField(self):
        return self.wait_until_element_clickable(By.XPATH, self.LOGIN_BUTTON)

    def getReviewButtonField(self):
        return self.driver.find_elements(By.XPATH, self.REVW_BUTTON)


    def enter_Username_Type_Field(self, username, password):
        self.getUserName().clear()
        self.getUserName().send_keys(username)
        x = datetime.datetime.now()
        self.log.info("****************************" + str(x) + "***************************")
        self.log.info("Successfully entered the username")
        time.sleep(4)
        self.getPasswordField().clear()
        self.getPasswordField().send_keys(password)
        self.log.info("successfully Entered the password")
        time.sleep(4)

    def enter_Login_Btn_Field(self):
        self.getLoginButtonField().click()
        self.log.info("Successfully Clicked on login button")
        time.sleep(8)

    def enter_Review_Btn_Field(self):
        time.sleep(6)
        # self.getReviewButtonField().click()

        # review_btn_field = self.driver.find_elements(By.XPATH, self.REVW_BUTTON)
        review_btn_field = self.getReviewButtonField()
        if len(review_btn_field) > 0:
            self.getReviewButtonField().click()
        else:
            self.log.info("Review button not displayed")
        # self.log.info(review_btn_field)



    def final_Login_Page_method(self, username, password):
        self.enter_Username_Type_Field(username, password)
        self.enter_Login_Btn_Field()
        self.enter_Review_Btn_Field()
        Link_Campaign_Page = Campaign_page(self.driver)
        return Link_Campaign_Page











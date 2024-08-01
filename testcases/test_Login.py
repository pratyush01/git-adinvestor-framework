# launch the adinvestor
# provide the login details
# Click on the review button
# Click on the menu tab for 1st menu
# Review: xpath- "//span[normalize-space()='Review Now']"
# Menu: Campaign: Xpath- "//span[contains(@class,'mr-2') and contains(text(),'Campaigns')]"


import time
import pytest
import softest
from pages.login_page import Login_page
from utilities.utils import Utils
from ddt import ddt, data, unpack, file_data

@pytest.mark.usefixtures("setup")
@ddt
class Testloginandverify(softest.TestCase):
    log = Utils.custlogger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Login_page(self.driver)

    # This code is to read data from excel and * infront of method will ensure and give us that this method will return list
    @data(*Utils.readDataFromExcel("E:\\Python\\PycharmProjects\\Adinvestor_framework\\testdata\\tdataexcel.xlsx.xlsx", "DemoSheet"))
    @unpack
    def testDemoLoginAndVerify(self, user1, pass1, client1):
        Link_Campaign_Page = self.lp.final_Login_Page_method(user1, pass1)
        self.log.info("Successfully entered the Loginpage and Password")
        Link_Campaign_Page.enter_Campaign_Page_Field()
        self.log.info("Clicked on Campaign page")
        Link_Campaign_Page.enter_Client_Dropdwn_Field(client1)
        self.log.info("Clicked on campaign client dropdown")
        Link_Campaign_Page.page_scroll()

    # # This code is to read data from csv
    # @data(*Utils.readDataFromCSV("E:\Python\PycharmProjects\Adinvestor_framework\testdata\tdataexcel.xlsx.xlsx",
    #                                   "DemoSheet"))
    # @unpack
    # def test_demo_explicit_wait(self, user1, pass1, client1):
    #     Link_Campaign_Page = self.lp.final_Login_Page_method(user1, pass1)
    #     self.log.info("Successfully entered the Loginpage and Password")
    #     Link_Campaign_Page.enter_Campaign_Page_Field()
    #     self.log.info("Clicked on Campaign page")
    #     Link_Campaign_Page.enter_Client_Dropdwn_Field(client1)
    #     self.log.info("Clicked on campaign client dropdown")
    #     Link_Campaign_Page.page_scroll()






    # This is for ddt framework where we using json format to read data-------------------------------------------->>
    # @file_data('../testdata/testdata.json')
    # def test_demo_explicit_wait(self, user1, pass1, client1):
    #     Link_Campaign_Page = self.lp.final_Login_Page_method(user1, pass1)
    #     self.log.info("Successfully entered the Loginpage and Password")
    #     Link_Campaign_Page.enter_Campaign_Page_Field()
    #     self.log.info("Clicked on Campaign page")
    #     Link_Campaign_Page.enter_Client_Dropdwn_Field(client1)
    #     self.log.info("Clicked on campaign client dropdown")
    #     Link_Campaign_Page.page_scroll()









    # # This is for ddt framework----------------------------------------------------------------------->>
    # @data(("analytics", "$uperSmile11", "Breakroom"), ("analytics", "$uperSmile11", "Bucks Media FlirtyAt40"))
    # @unpack
    # def test_demo_explicit_wait(self, user1, pass1, client1):
    #     Link_Campaign_Page = self.lp.final_Login_Page_method(user1, pass1)
    #     self.log.info("Successfully entered the Loginpage and Password")
    #     Link_Campaign_Page.enter_Campaign_Page_Field()
    #     self.log.info("Clicked on Campaign page")
    #     Link_Campaign_Page.enter_Client_Dropdwn_Field(client1)
    #     self.log.info("Clicked on campaign client dropdown")
    #     Link_Campaign_Page.page_scroll()





#
#     # This is normal framework where we are giving the data static/hardcoded.
#     def test_demo_explicit_wait(self, user1, pass1, client1):
#         Link_Campaign_Page = self.lp.final_Login_Page_method("analytics", "$uperSmile11")
#         self.log.info("Successfully entered the Loginpage and Password")
#         Link_Campaign_Page.enter_Campaign_Page_Field()
#         self.log.info("Clicked on Campaign page")
#         Link_Campaign_Page.enter_Client_Dropdwn_Field("Breakroom")
#         self.log.info("Clicked on campaign client dropdown")
#         Link_Campaign_Page.page_scroll()












        # Launching the browser
        # Providing the Login details
        # Campaign Page Methods Starts here -->
        # Clicking on the review button
        # Clicking on the Menu button

































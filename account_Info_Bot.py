
from selenium import webdriver          #webdriver used to interract with webpages
from time import sleep 


### A bot to return basic information about the user profile 
class InstaBot: 
    def __init__(self, uName, pWord):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        
        self.uName = uName
        sleep(2)

        '''
        #Getting Log in button by xcode and clicking
        #button is found by X query for a link that contains 'log in' 
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        '''

        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(uName)
        
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pWord)

        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        sleep(2)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()

        sleep(3)

             



#your username and password
bot1 = InstaBot('', '')
#bot1.get_followers()

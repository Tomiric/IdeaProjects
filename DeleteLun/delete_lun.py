from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://172.16.11.35/auth")
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("admin")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_css_selector("button.button-text.button-text-large").click()

        driver.find_element_by_css_selector("span.icon-44.icon-44-protocol").click()
        time.sleep(1)
        driver.find_element_by_css_selector("span.icon-32.icon-32-fc").click()
        time.sleep(3)
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/p/span[2]").click()
        driver.find_element_by_css_selector("span.button-icon-image > span.icon-44.icon-44-settings").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div/div[2]/div[2]/div/div/div[7]/div/button").click()
        driver.find_element_by_xpath("//input").clear()
        driver.find_element_by_xpath("//input").send_keys("ok")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        time.sleep(2)
        driver.find_element_by_css_selector("span.icon-44.icon-44-database").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-volume").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='main']/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div[1]").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_css_selector("button.button-text").click()
        time.sleep(2)
        driver.find_element_by_css_selector("input.input").clear()
        driver.find_element_by_css_selector("input.input").send_keys("ok")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        time.sleep(2)
        driver.find_element_by_css_selector("span.icon-44.icon-44-database").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-pool").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[3]/button/span/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[11]/div/button").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div[2]/div[2]/div[2]/div/form/div[2]/div/input").clear()
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div[2]/div[2]/div[2]/div/form/div[2]/div/input").send_keys("ok")
        driver.find_element_by_xpath("//div[4]/div/button").click()


def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


















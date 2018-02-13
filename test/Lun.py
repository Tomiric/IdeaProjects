from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


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
        driver.find_element_by_css_selector("span.icon-44.icon-44-database").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-pool").click()
        driver.find_element_by_css_selector("span.icon-44.icon-44-add").click()
        time.sleep(3)
        driver.find_element_by_xpath("//input[@id='name']").clear()
        driver.find_element_by_xpath("//input[@id='name']").send_keys("autotest")
        time.sleep(3)
        driver.find_element_by_css_selector("label.checkbox-label").click()
        driver.find_element_by_css_selector("div.multi-item.multi-item-active > div.checkbox > label.checkbox-label").click()
        driver.find_element_by_css_selector("button.button-text").click()
        driver.find_element_by_css_selector("div.loader-spinner").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div[2]/div").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-volume").click()
        driver.find_element_by_css_selector("span.icon-44.icon-44-add").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("vol1")
        time.sleep(1)
        driver.find_element_by_id("size").click()
        driver.find_element_by_id("size").clear()
        driver.find_element_by_id("size").send_keys("100")
        driver.find_element_by_css_selector("label.checkbox-label").click()
        driver.find_element_by_css_selector("label.checkbox-label").click()
        driver.find_element_by_xpath("//div[6]/div[2]/div/select").click()
        driver.find_element_by_xpath("//div[6]/div[2]/div/select").click()
        driver.find_element_by_css_selector("button.button-text").click()
        time.sleep(2)
        driver.find_element_by_css_selector("span.icon-44.icon-44-protocol").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-fc").click()
        time.sleep(5)
        driver.find_element_by_css_selector("span.icon-44.icon-44-add").click()
        time.sleep(3)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='volume']/select").click()
        time.sleep(2)
        Select(driver.find_element_by_xpath("//div[@id='volume']/select")).select_by_visible_text("autotest/vol1")
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='volume']/select").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div/div[2]/div[2]/div/form/div[3]/div[2]/input").click()
        driver.find_element_by_id("lun").clear()
        driver.find_element_by_id("lun").send_keys("11")
        driver.find_element_by_css_selector("button.button-text").click()
        #driver.find_element_by_xpath("//div[3]/a/span").click()
        #driver.find_element_by_xpath("//div[2]/div[3]/a/span").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/p/span[2]").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button/span/span").click()
        driver.find_element_by_xpath("//div[7]/div/button").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div[2]/div[2]/div[2]/div/form/div[2]/div/input").clear()
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div[2]/div[2]/div[2]/div/form/div[2]/div/input").send_keys("ok")
        driver.find_element_by_xpath("//div[4]/div/button").click()
        driver.find_element_by_xpath("//div[2]/a/span").click()
        driver.find_element_by_xpath("//div[2]/div[4]/a/span").click()
        driver.find_element_by_xpath("//div[6]/div").click()
        driver.find_element_by_xpath("//div[2]/button/span/span").click()
        driver.find_element_by_xpath("//div[9]/div/button").click()
        driver.find_element_by_css_selector("input.input").clear()
        driver.find_element_by_css_selector("input.input").send_keys("ok")
        driver.find_element_by_css_selector("div.form-cell.form-cell-center.form-cell-100 > button.button-text").click()
        driver.find_element_by_xpath("//div[2]/div[2]/a/span").click()
        driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//div[3]/button/span/span").click()
        driver.find_element_by_xpath("//div[11]/div/button").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div[2]/div[2]/div[2]/div/form/div[2]/div/input").clear()
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div[2]/div[2]/div[2]/div/form/div[2]/div/input").send_keys("ok")
        driver.find_element_by_xpath("//div[4]/div/button").click()

def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
        unittest.main()

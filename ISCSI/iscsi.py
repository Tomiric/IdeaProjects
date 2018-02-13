from selenium import webdriver
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
        driver.find_element_by_css_selector("span.icon-44.icon-44-database").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-volume").click()
        driver.find_element_by_css_selector("span.icon-44.icon-44-add").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("vol2")
        time.sleep(1)
        driver.find_element_by_id("size").click()
        driver.find_element_by_id("size").clear()
        driver.find_element_by_id("size").send_keys("100")
        driver.find_element_by_css_selector("label.checkbox-label").click()
        driver.find_element_by_css_selector("label.checkbox-label").click()
        driver.find_element_by_xpath("//div[6]/div[2]/div/select").click()
        driver.find_element_by_xpath("//div[6]/div[2]/div/select").click()
        driver.find_element_by_css_selector("button.button-text").click()
        time.sleep(3)
        driver.find_element_by_css_selector("span.icon-44.icon-44-protocol").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-iscsi").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='volume']").click()
        time.sleep(2)
        Select(driver.find_element_by_xpath("//div[@id='volume']/select")).select_by_visible_text("testPMI/vol2")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='lun']").clear()
        driver.find_element_by_xpath("//input[@id='lun']").send_keys("12")
        time.sleep(2)
        driver.find_element_by_xpath("//body[@id='main']/div/div[3]/div/div[2]/div[2]/div/form/div[5]/div/button").click()
        time.sleep(2)
        driver.find_element_by_css_selector("span.icon-44.icon-44-security").click()
        driver.find_element_by_css_selector("span.icon-32.icon-32-access").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/button/span/span").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("ClientISCSI")
        driver.find_element_by_css_selector("button.button-text").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//body[@id='main']/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("//body[@id='main']//div[3]/div[2]/div[1]/button[1]/span[1]/span[1]").click()
        driver.find_element_by_id("iqn").clear()
        driver.find_element_by_id("iqn").send_keys("iqn.1998-01.com.vmware:srv31-0d6b969d")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        driver.find_element_by_css_selector("button.button-text").click()





def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True

def is_alert_present(self):
    try: self.driver.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True

def close_alert_and_get_its_text(self):
    try:
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally: self.accept_next_alert = True

def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


















